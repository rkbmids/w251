import numpy as np
from PIL import Image
import tensorflow as tf
import numpy as np
import time
#from tf_trt_models.detection import download_detection_model, build_detection_graph
import paho.mqtt.client as mqtt
import cv2
import os
HOST="broker"
PORT=1883
TOPIC="facedetect"

FROZEN_GRAPH_NAME='/model_download/frozen_inference_graph_face.pb'
INPUT_NAME='image_tensor'
BOXES_NAME='detection_boxes'
CLASSES_NAME='detection_classes'
SCORES_NAME='detection_scores'
MASKS_NAME='detection_masks'
NUM_DETECTIONS_NAME='num_detections'
THRESHOLD=0.5

input_names = [INPUT_NAME]
output_names = [BOXES_NAME, CLASSES_NAME, SCORES_NAME, NUM_DETECTIONS_NAME]
def on_connect(clnt, user, flags, rc):
    print("connected with rc:" + str(rc))

client = mqtt.Client()
client.on_connect = on_connect
client.connect(HOST, PORT)

#cascade = cv2.CascadeClassifier('/usr/share/opencv/haarcascades/haarcascade_frontalface_default.xml')


output_dir=''
frozen_graph = tf.GraphDef()
with open(os.path.join(output_dir, FROZEN_GRAPH_NAME), 'rb') as f:
  frozen_graph.ParseFromString(f.read())

tf_config = tf.ConfigProto()
tf_config.gpu_options.allow_growth = True
tf_sess = tf.Session(config=tf_config)
tf.import_graph_def(frozen_graph, name='')
tf_input = tf_sess.graph.get_tensor_by_name(input_names[0] + ':0')
tf_scores = tf_sess.graph.get_tensor_by_name('detection_scores:0')
tf_boxes = tf_sess.graph.get_tensor_by_name('detection_boxes:0')
tf_classes = tf_sess.graph.get_tensor_by_name('detection_classes:0')
tf_num_detections = tf_sess.graph.get_tensor_by_name('num_detections:0')

capture = cv2.VideoCapture(1)
while(True):
    ret, frame = capture.read()
    if ret == 0:
        break
    image = cv2.flip(frame, 1)
    image_np = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image_np_expanded = np.expand_dims(image_np, axis=0)
    scores, boxes, classes, num_detections = tf_sess.run(
        [tf_scores, tf_boxes, tf_classes, tf_num_detections],
        feed_dict={
            tf_input: image_np_expanded
            })
    boxes = boxes[0] # index by 0 to remove batch dimension
    scores = scores[0]
    classes = classes[0]
    num_detections = num_detections[0]
    faces = []
    for i in range(int(num_detections)):
        if scores[i] < DETECTION_THRESHOLD:
            box = boxes[i] * np.array([image_resized.shape[0],
                image_resized.shape[1], image_resized.shape[0],
                image_resized.shape[1]])
            faces += box

    for (x,y,w,h) in faces:
        face = frame[y:y+h, x:x+w]
        print("\nFound a face!\nShape: ", face.shape, '\nType: ', face.dtype)
        rc,jpg = cv2.imencode('.png', face)
        msg = jpg.tobytes()
        client.publish(TOPIC, payload=msg, qos=0, retain=False)
        print("Published Message!")
