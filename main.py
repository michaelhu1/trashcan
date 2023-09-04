from detect import *
from sensors import *
from servos import *
from display import *
from threading import Thread
class Prediction:
    def __init__(self):
        self.prediction = ''

prediction = Prediction()
display = Display(prediction)
displaythread = Thread(target = display.main)
is_person = False

#ultrasonic_setup()
#ultrasonic_setup()

model = model_setup()    
camera = camera_setup()
clear_image()
displaythread.start()


"""while is_person == False:
    distance = ultrasonic_ping()
    if distance <= 10 :
        is_person == True
        opendoor()
          """
#if is_person == True:
result =  classify(model,camera)
if len(result["predictions"]) == 0:
    print("Error: Nothing detected")
    prediction.prediction = "Fail"
else:
    prediction_object = result["predictions"][0]
    prediction.prediction = prediction_object["class"]
    print(prediction.prediction)      
clear_image()
    #openbin(prediction)
    #code for pusher push trash to correct bin
    
    
    
