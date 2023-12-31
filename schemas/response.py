from typing import Optional, TypedDict

from enum import Enum

class ResponseCodes(Enum):
    OK=200
    BAD_REQUEST=400
    NOT_FOUND=404
class Response(TypedDict):
    statusCode:int
    headers:Optional[str]
    body:str
