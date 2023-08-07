from picamera2 import Picamera2
from roboflow import Roboflow
import os
from time import sleep


def model_setup():
    rf = Roboflow(api_key="nRKJI75lSbTjbJv55RPY")
    project = rf.workspace().project("classify-trash-3")
    model = project.version(9).model
    return model

def camera_setup():
    camera = Picamera2()
    camera_config = camera.create_still_configuration(main = {"size": (640,640)},lores={"size":(640,640)}, display="lores")
    camera.configure(camera_config)
    return camera

def classify(model, camera):
      
    camera.start()
    sleep(5)
    camera.capture_file("/home/michaelhu1/Desktop/image.jpg")
    return model.predict("/home/michaelhu1/Desktop/image.jpg",confidence = 40, overlap = 30).json()
    
def clear_image():
    if os.path.isfile("/home/michaelhu1/Desktop/image.jpg"):
        os.remove("/home/michaelhu1/Desktop/image.jpg")



