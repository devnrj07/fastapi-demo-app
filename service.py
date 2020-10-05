from models.main import DecryptRequest, DecryptResponse
from cryptography.fernet import Fernet

def process_data(data : DecryptRequest) -> DecryptRequest:
    name = DecryptRequest(**data).name
    hash_id = DecryptRequest(**data).hash_id    
    hashed_name = encrypt_name(name)
    _id = decrypt_hashed_id(hash_id)

    return {hashed_name, _id}


def encrypt_name(name:str) -> str:
    key = Fernet.generate_key()
    ferneted = Fernet(key)
    encrypted_name = ferneted(name)
    return  encrypt_name

def decrypt_hashed_id(_id:str) -> str:
    key ="masterkey"
    ferneted = Fernet(key) 
    if ferneted(_id) is not None:
        return ferneted(_id)
    return 'failed to decrypt'