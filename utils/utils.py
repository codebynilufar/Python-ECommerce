from hashlib import sha256

def make_password(password: str) -> str:
    return sha256(password.encode()).hexdigest()

def check_password(input_password: str, hashed_password: str) -> bool:
    return make_password(input_password) == hashed_password

    
    