from pydantic import BaseModel

class DecryptRequest(BaseModel):
    name : str
    hash_id : str

class DecryptResponse(BaseModel):
    hashed_name : str
    _id:str