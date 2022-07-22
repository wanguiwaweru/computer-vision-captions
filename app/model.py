from datetime import datetime
from typing import Optional
from pydantic import BaseModel,HttpUrl

class ApiResponse:
    status_code: int
    message: str
    request_id: str
    captions: list

class ImageDetails():
    url: str
    image_format: str
    width: int
    height : int
    total_bytes: int
    image_binary: int
    sha256_signature: str

class Caption():
    alt_text: str
    confidence: float

class AzureCVResponse():
    request_id: str
    captions: Caption

class APIRequest(BaseModel):
    url: Optional[HttpUrl]
    request_id: Optional[str]

    class Config:
        arbitrary_types_allowed = True
        schema_extra = {
            "example":{
                "url": "https://images.unsplash.com/photo-1655747450799-ac8c561f256a?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxleHBsb3JlLWZlZWR8OXx8fGVufDB8fHx8&auto=format&fit=crop&w=600&q=60",
                "request_id": "1234-04x4-894"
            }
        }

class RequestMetadata(APIRequest):
    root_operation_id: Optional[str]
    request_time: Optional[datetime]
    response: Optional[ApiResponse]
    azure_cv_response: Optional[AzureCVResponse]
    image: Optional[ImageDetails]