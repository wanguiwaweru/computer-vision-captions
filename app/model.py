from datetime import datetime
from typing import TypeVar,Optional
from pydantic import BaseModel

APIResponse = TypeVar('APIResponse')

class APIResponse:
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

class Caption():
    alt_text: str
    confidence: float

class AzureCVResponse():
    request_id: str
    captions: Caption

class APIRequest(BaseModel):
    url: Optional[str]
    root_operation_id: Optional[str]
    request_id: Optional[str]
    request_time: Optional[datetime]
    response: Optional[APIResponse]
    azure_cv_response: Optional[AzureCVResponse]

    class Config:
        arbitrary_types_allowed = True