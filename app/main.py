from fastapi import FastAPI
from model import ImageUrl
from PIL import Image
from io import BytesIO
import requests
import uuid


app =  FastAPI()
SUBSCRIPTION_KEY = 'a6498ac0712546258fd220d13d2e90bb'
ENDPOINT = 'https://cv-alt-text-generator.cognitiveservices.azure.com/'
REQUEST_URL = ENDPOINT +'vision/v3.2/describe?maxCandidates=4&language=en&model-version=latest'
headers = {'Ocp-Apim-Subscription-Key':SUBSCRIPTION_KEY}
params = {'visualFeatures':'Categories,Description,Color'}

supported_image_formats = ("PNG", "JPEG", "JPG","BMP","GIF")

class ImageDetails():
    url: str
    image_format: str
    width: int
    height : int
    total_bytes: int
    image_binary: int

class Caption():
    alt_text: str
    confidence: float

class Response():
    captions: Caption
    request_id: str
    status: str
   
@app.post("/api")
async def root(imageUrl: ImageUrl):
    try:
        if is_valid_image(download_image_from_url(imageUrl.url)) == True:
            return { "response": get_image_description(imageUrl.url)}
    
    except Exception as e:
        return e

def download_image_from_url(url):
    # validate url before proceeding
    # validate image download response
    # 3XX, 4xx, 5XX

    response = requests.get(url)

    if response.status_code == 200 or response.status_code == 201:
        imageDetails = ImageDetails()
        imageDetails.image_binary = response.content
        return imageDetails
    
    elif response.status_code >= 500 and response.status_code < 600:
        return {"details": "server error"}
    
    return None

def is_valid_image(imageDetails, max_file_size=4000000):
    if imageDetails is None:
        return "Image details not found"
    
    if imageDetails.image_binary is None:
        return "image binary is missing or invalid"
    
    try:
        img = Image.open(BytesIO(imageDetails.image_binary))
        imageDetails.width = img.width
        imageDetails.height = img.height
        imageDetails.image_format = img.format
        imageDetails.total_bytes = len(imageDetails.image_binary)
        
        if imageDetails.image_format in supported_image_formats:
            if int(imageDetails.total_bytes) <= max_file_size:
                if (imageDetails.width and imageDetails.height > 50):
                    return True
                else:
                    return "Image should be greater than 50 x 50"
            else:
                return "Image file size must be less than 4MB"
        else:
            return "Invalid image format."
    except Exception as e:
        return {"error" : e}

def get_image_description(url):
    data = {'url':url}
    response = requests.post(REQUEST_URL,headers=headers,params=params,json=data)
    response.raise_for_status()
    analysis = response.json()
    results = Response()
    results.captions = Caption()

    results.status = response.status_code
    results.request_id = uuid.uuid4()
    results.captions.alt_text = analysis['description']['captions'][0]['text'].capitalize()
    results.captions.confidence = "{:.2f}".format(analysis['description']['captions'][0]['confidence']) 
    return results