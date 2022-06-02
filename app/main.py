from app.model import APIRequest, APIResponse, Caption, ImageDetails
from fastapi import FastAPI
from PIL import Image
from io import BytesIO
import requests


app =  FastAPI()
SUBSCRIPTION_KEY = 'a6498ac0712546258fd220d13d2e90bb'
ENDPOINT = 'https://cv-alt-text-generator.cognitiveservices.azure.com/'
REQUEST_URL = ENDPOINT +'vision/v3.2/describe?maxCandidates=4&language=en&model-version=latest'
headers = {'Ocp-Apim-Subscription-Key':SUBSCRIPTION_KEY}
params = {'visualFeatures':'Categories,Description,Color'}

supported_image_formats = ("PNG", "JPEG", "JPG","BMP","GIF")

res = APIResponse()

@app.post("/api")
async def root(request: APIRequest):
    try:
        res.status_code = 200
        res.request_id = request.request_id

        if is_valid_image(download_image_from_url(request.url)) == True:
            res.message = "Image downloaded successfully"
            res.captions = get_image_description(request.url)
    except Exception as e:
        print(e)
    
    return res

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
        res.status_code = 500
        res.message = "server error occurred"
    
    return None

def is_valid_image(imageDetails, max_file_size=4000000):
    res.status_code = 500

    if imageDetails is None:
        res.message = "Image details not found"
        return
    
    if imageDetails.image_binary is None:
        res.message = "image binary is missing or invalid"
        return
    
    try:
        img = Image.open(BytesIO(imageDetails.image_binary))
        imageDetails.width = img.width
        imageDetails.height = img.height
        imageDetails.image_format = img.format
        imageDetails.total_bytes = len(imageDetails.image_binary)
        
        if imageDetails.image_format in supported_image_formats:
            if int(imageDetails.total_bytes) <= max_file_size:
                if (imageDetails.width and imageDetails.height > 50):
                    res.status_code = 200
                    return True
                else:
                    res.message = "Image should be greater than 50 x 50"
            else:
                res.message = "Image file size must be less than 4MB"
        else:
            return "Invalid image format."
    except Exception as e:
        return {"error" : e}

def get_image_description(url):
    captions = list()

    data = {'url':url}
    response = requests.post(REQUEST_URL,headers=headers,params=params,json=data)
    response.raise_for_status()
    analysis = response.json()

    for i in range(len(analysis['description']['captions'])):
        caption = Caption()
        caption.alt_text = analysis['description']['captions'][i]['text'].capitalize()
        caption.confidence = "{:.2f}".format(analysis['description']['captions'][i]['confidence'])
        captions.append(caption)
    
    return captions