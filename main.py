from detect import *

model = model_setup()
camera = camera_setup()

clear_image()

result =  classify(model,camera)
print(result)
clear_image()