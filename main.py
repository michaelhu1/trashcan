from detect import *


model = model_setup()
camera = camera_setup()

clear_image()

result =  classify(model,camera)
prediction = result["predictions"][0]
print(prediction["class"])

clear_image()