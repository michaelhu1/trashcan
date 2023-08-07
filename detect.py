from picamera2 import Picamera2
import tty, sys, termios
from roboflow import Roboflow
import os
from time import sleep

if os.path.isfile("/home/michaelhu1/Desktop/image.jpg"):
        os.remove("/home/michaelhu1/Desktop/image.jpg")


rf = Roboflow(api_key="nRKJI75lSbTjbJv55RPY")
project = rf.workspace().project("classify-trash-3")
model = project.version(9).model

camera = Picamera2()
camera_config = camera.create_still_configuration(main = {"size": (640,640)},lores={"size":(640,640)}, display="lores")
camera.configure(camera_config)

filedescriptors = termios.tcgetattr(sys.stdin)
tty.setcbreak(sys.stdin)
x = 0
while 1:
        x = sys.stdin.read(1)[0]
        if x == 'x':
                camera.start()
                sleep(5)
                camera.capture_file("/home/michaelhu1/Desktop/image.jpg")
                print(model.predict("/home/michaelhu1/Desktop/image.jpg",confidence = 40, overlap = 30).json())
                if os.path.isfile("/home/michaelhu1/Desktop/image.jpg"):
                        os.remove("/home/michaelhu1/Desktop/image.jpg")
        if x == 'b':
                break

termios.tcsetattr(sys.stdin, termios.TCSADRAIN, filedescriptors)
