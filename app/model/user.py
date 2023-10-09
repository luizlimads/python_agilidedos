from hashlib import sha256
import os

from dotenv import load_dotenv
load_dotenv()

class User:
    name:str
    login:str
    password:str
    email:str

    def __init__(self, name = None, login = None, password = None, email = None,*args, **kwargs):
        self.name = name
        self.login = login
        self.password = self.hashed_password(password) if password else None
        self.email = email

    
    def hashed_password(self,password) -> str:
        salt = os.environ["salt"]
        password_salt = str(salt+'@'+password)
        hash_password = sha256(password_salt.encode())
        return hash_password.hexdigest()
        

    def __str__(self):
        return (f'{self.name} {self.login} {self.password} {self.email}')