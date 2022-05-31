from pydantic import BaseModel,HttpUrl
from typing import Optional, Union

class ImageUrl(BaseModel):
    url:HttpUrl
    base64: Optional[str]
