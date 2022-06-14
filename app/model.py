from datetime import datetime
from typing import Optional

from pydantic import BaseModel

class ApiResponse():
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
    sha256_signature : str

class Caption():
    alt_text: str
    confidence: float

class AzureCVResponse():
    request_id: str
    captions: Caption

class APIRequest(BaseModel):
    root_operation_id: Optional[str]
    request_id: Optional[str]
    request_time: Optional[datetime]
    response: Optional[ApiResponse]
    azure_cv_response: Optional[AzureCVResponse]
    url: Optional[str]
    image: Optional[ImageDetails]
    
    class Config:
        arbitrary_types_allowed = True