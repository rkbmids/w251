# Setup

## On the Jetson
Once Docker is installed and running, navigate to the edge folder in the repo and run:
```
chmod 777 jetson.sh
./jetson.sh
```
## On the Cloud VM
Once Docker is installed and running, navigate to the cloud folder in the repo. To bind cloud storage to the server, run:
```
chmod 777 storage.sh
./storage.sh
```
Then, to run the rest of the service, run:
```
chmod 777 cloud.sh
./cloud.sh
```
## Topics
The local topic on the Jetson is called facedetect. The forwarder script publishes the messages from facedetect to cloudfaces remotely on the server.

## QOS
Because I didn't want a huge backlog of images to accumulate on the system, I used the default QOS value of 0, which is 'fire and forget'. In a production scenario, I would probably use a QOS of 1 instead, which guarantees delivery.
