from pydantic import BaseModel,HttpUrl
from typing import Optional, Union

class APIRequest(BaseModel):
    url:HttpUrl
    base64: Optional[str]
    request_id: str

class APIResponse():
    status_code: int
    message: str
    request_id: str
    captions: Optional[list]

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
