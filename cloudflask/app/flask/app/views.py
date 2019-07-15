from app import app
import os

@app.route("/")
def index():
    #HOMEPAGE
    #Input user name
    #Option to either view results or review images
    pass


@app.route("/view_data/")
def view_data():
    #Plot tracking proportion of slouching - use D3 line plot with tooltips for
    #each data point and green to red color map for 0-100% slouching
    pass

@app.route("/review_images/")
def review_images():
    #For each image id for a given user not in the image_feedback table,
    #present image and classification with links to agree or disagree.
    pass
