'''

This is the backend for the project econova
this back will process images and tell the medicinal benefits of the plants

'''

import ai_process as ai
import api_reponse as ar



class plants:

    def __init__(self, name): 
        self.name = name


    def imageProcess(self, name):
        return ar.image_process.apiResponse(name)        

    def openAi_response(self, plant_name):
        ai.ai_response.ai_processing(plant_name)
    
if __name__=="__main__":
    input_image = plants("") # ENTER THE URL OF IMAGE HERE
    img_name = input_image.imageProcess(input_image.name)
    input_image.openAi_response(img_name)