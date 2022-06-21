from app.model import APIRequest, ApiResponse, Caption, ImageDetails,AzureCVResponse
from datetime import datetime
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from PIL import Image
from io import BytesIO
from caching import *
import hashlib
import requests
import config
import uuid
import json


app =  FastAPI()

supported_image_formats = ("PNG", "JPEG", "JPG","BMP","GIF")

@app.post("/api")
async def root(httpRequest: Request,request:APIRequest):
    try:
        initialize_request(request)
       
        global res
        res = ApiResponse()

        if headers_valid(httpRequest.headers):
            res.status_code = 400
            res.message = "Missing or invalid X-Caller-ID"
        elif is_valid_image(download_image_from_url(request.url)) == True:
            request.image = imageDetails
            cached_image = get_response_from_cache(request.image.sha256_signature)
           
            if cached_image is None:
                request.azure_cv_response = get_image_description(request.url)
                res.captions =  request.azure_cv_response.captions
                
                # cache information about this image
                client.setex(request.image.sha256_signature, timeout, json.dumps(jsonable_encoder(request.azure_cv_response)))
                    
            else:
                # pick information from cached image
                # if client already sent the request, return cached response instead
            
                res.captions = json.loads(cached_image)['captions']
            res.request_id = request.request_id
            res.message = "Image processed successfully."

    except Exception as e:
        # log exception details
        return e
    finally:

        request.response = res
    return JSONResponse(status_code = res.status_code, content = jsonable_encoder(res))

def headers_valid(headers):
    if headers.get('X-Caller-ID') is None or str(headers.get('X-Caller-ID')).isspace():
        return True
    
    return False

def initialize_request(request):
    try:
        request.request_time = datetime.now()
        request.root_operation_id = uuid.uuid4()     
    except Exception as e:
        print(e)
        raise e

def download_image_from_url(url):
    # validate url before proceeding
    # validate image download response
    # 3XX, 4xx, 5XX

    response = requests.get(url)
   
    if response.status_code == 200 or response.status_code == 201:
        global imageDetails
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
                    imageDetails.sha256_signature = hashlib.sha256(imageDetails.image_binary).hexdigest()
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
    response = requests.post(config.REQUEST_URL,headers=config.headers,params=config.params,json=data)     
    response.raise_for_status()
    analysis = response.json()

    for i in range(len(analysis['description']['captions'])):
        caption = Caption()
        caption.alt_text = analysis['description']['captions'][i]['text'].capitalize()
        caption.confidence = "{:.2f}".format(analysis['description']['captions'][i]['confidence'])
        captions.append(caption)
    
    azure_cv_response = AzureCVResponse()
    azure_cv_response.request_id = analysis['requestId']
    azure_cv_response.captions = captions
    return azure_cv_response