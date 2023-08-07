from detect import *
import json

model = model_setup()
camera = camera_setup()

clear_image()

result =  classify(model,camera)
result_dict = json.loads(result)
prediction = result_dict["predictions"][0]
print(prediction["class"])

clear_image()