from detect import *
from sensors import *
from servos import *
 
is_person = False

ultrasonic_setup()
ultrasonic_setup()

model = model_setup()
camera = camera_setup()
clear_image()



while is_person == False:
    distance = ultrasonic_ping()
    if distance <= 10 :
        is_person == True
        opendoor()
          
if is_person == True:
    result =  classify(model,camera)
    if len(result["predictions"]) == 0:
        print("Error: Nothing detected")
    else:
        prediction = result["predictions"][0]
        print(prediction["class"])      
    clear_image()
    openbin(prediction)
    #code for pusher push trash to correct bin
    
    
    
