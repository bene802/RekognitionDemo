import boto3
import requests
from pprint import pprint
client = boto3.client('rekognition')

image_url = 'https://s3.amazonaws.com/detect-analyze-face-rekognition-tutorial/detect-analyze-faces-rekognition-sample1.jpg'


request = requests.get(image_url)
image_bytes = request.content
res = client.detect_faces(Image={'Bytes': image_bytes})

pprint(res)
