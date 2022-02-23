
from pydantic import BaseModel

class Feed(BaseModel):
    text: str

    class Config:
        orm_mode = True


class Feed(BaseModel):
    text: str
    
    class Config:
        orm_mode = True