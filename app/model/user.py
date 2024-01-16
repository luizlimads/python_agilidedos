import os
import json

from hashlib import sha256
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

    @staticmethod
    def from_json(json_data):
        """
        Método estático para criar uma instância de User a partir de um dicionário ou JSON.

        Args:
            json_data (dict): Dados do usuário em formato de dicionário ou JSON.

        Returns:
            User: Instância da classe User.

        """
        return User(**json_data)


       
    def hashed_password(self,password) -> str:
        """
        Método para criação de senhas.

        Args:
            passord (str): string contendo o password original.

        Returns:
            hash_password (str): Nova senha com hash.
        """
        salt = os.environ["salt"]
        password_salt = str(salt+'@'+password)
        hash_password = sha256(password_salt.encode())
        return hash_password.hexdigest()
            
    def to_json(self):
        """
        Método para retornar velores na forma de Json.

        Args:
            None.

        Returns:
            Json: Json com as variáveis do User.

        """

        user_dict = {key: value for key, value in self.__dict__.items() if value is not None}
        return json.dumps(user_dict, indent=4)

    def __str__(self):
        return (f'{self.name} {self.login} {self.password} {self.email}')