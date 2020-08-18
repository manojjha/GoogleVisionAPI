import os, io
# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types
import pandas as pd
from enum import Enum
import base64

from google.oauth2 import service_account

credentials = service_account.Credentials. from_service_account_file('kal-kal-1532846232334-738abd5f7e5a.json')
client = vision.ImageAnnotatorClient(credentials=credentials)

#os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'kal-kal-1532846232334-738abd5f7e5a.json'
#client = vision.ImageAnnotatorClient()
class FeatureType(Enum):
    PAGE = 1
    BLOCK = 2
    PARA = 3
    WORD = 4
    SYMBOL = 5

FOLDER_PATH = r'C:\Users\mjha3\Desktop\Django_project\VisionAPI_Test\test1\Test_Image_Samples'
IMAGES_FILE = 'test1.jpeg'
FILE_PATH = os.path.join(FOLDER_PATH, IMAGES_FILE)
#print(FILE_PATH)

with io.open(FILE_PATH, 'rb') as image_file:
    content = image_file.read()

image_content = vision.types.Image(content=content)
response = client.document_text_detection(image=image_content)
document = response.full_text_annotation
#print(response)
print(document)

# Collect specified feature bounds by enumerating all document features
for page in document.pages:
    for block in page.blocks:
        for paragraph in block.paragraphs:
            for word in paragraph.words:
                for symbol in word.symbols:
                    if (feature == FeatureType.SYMBOL):
                        bounds.append(symbol.bounding_box)

                if (feature == FeatureType.WORD):
                    bounds.append(word.bounding_box)

            if (feature == FeatureType.PARA):
                bounds.append(paragraph.bounding_box)

        if (feature == FeatureType.BLOCK):
            bounds.append(block.bounding_box)



'''for page in pages:
    for block in page.blocks:
        print('Block confidence:', block.confidence)

        for paragraph in block.paragraphs:
            #print('Paragraph confidence:', paragraph.confidence)

            for word in paragraph.words:
                word_text = ''.join([symbol.text for symbol in word.symbols])

                #print('Word text: {0} (confidence: {1}'.format(word_text, word.confidence))

                #for symbol in word.symbols:
                    #print('\tSymbol: {0} (confidence: {1}'.format(symbol.text, symbol.confidence))'''




