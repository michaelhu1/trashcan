from detect import *


model = model_setup()
camera = camera_setup()

clear_image()

result =  classify(model,camera)
if len(result["predictions"]) == 0:
    print("Error: Nothing detected")
else:
    prediction = result["predictions"][0]
    print(prediction["class"])

clear_image()