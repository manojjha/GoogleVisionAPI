def detect_text(path):
    """Detects text in the file."""
    from google.cloud import vision
    import io, os
    import json

    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'kal-kal-1532846232334-738abd5f7e5a.json'

    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    print('Texts:')

    for text in texts:
        print('\n"{}"'.format(text.description))

        vertices = (['({},{})'.format(vertex.x, vertex.y)
                    for vertex in text.bounding_poly.vertices])

        #print('bounds: {}'.format(','.join(vertices)))
    
    #export results to JSON file
    with open('image_results.json', 'w') as outputjson:
        json.dump(vertices, outputjson, ensure_ascii=False)

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))

#file_name = os.path.abspath('test2.jpg')

file_name = 'test1.jpeg'
detect_text(file_name)