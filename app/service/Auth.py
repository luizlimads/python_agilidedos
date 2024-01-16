
import jwt
import datetime
import os
import json

from flask import jsonify, request
from functools import wraps

from app.model.user import User

def token_required(f):
   """
    Decorador para autenticação por token.

    Este decorador verifica a presença e validade do token de acesso em cookies.
    Se o token for válido, ele extrai as informações do usuário e as passa para a função decorada.

    Args:
        f (Callable): Função a ser decorada.

    Returns:
        Callable: Função decorada.

    Raises:
        ValueError: Se as informações do usuário no token não forem do tipo User.
        jwt.ExpiredSignatureError: Se o token estiver expirado.
        jwt.InvalidTokenError: Se o token for inválido.

    Example:
        @token_required
        def my_protected_endpoint(user_data: User, *args, **kwargs):
            # Código protegido aqui

    """
   @wraps(f)
   def decorator(*args, **kwargs) -> User:
       token = None
       if 'x-access-tokens' in request.cookies:
            token = request.cookies['x-access-tokens']
 
       if not token:
           return jsonify({'message': 'a valid token is missing'})
       
       try:
           data = jwt.decode(token, key = os.environ["secret_key"], algorithms=["HS256"])
           user_data = User(**json.loads(data.get('user', {})))
           
           if not isinstance(user_data, User):
            raise ValueError('Invalid user data')
       
       except jwt.ExpiredSignatureError:
        return jsonify({'message': 'token has expired'})
       except jwt.InvalidTokenError:
        return jsonify({'message': 'invalid token'})
       except ValueError as e:
        return jsonify({'message': str(e)})
 
       return f(user_data,*args, **kwargs)
   return decorator

def parametros_auth(user: User):
    parametres = {
        'key' : 'x-access-tokens',
        'value' : generate_token(user),
        'httponly': True
    }
    return parametres    

def generate_token(user: User):
    token = jwt.encode(payload={'user' :user.to_json() , 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=45)}, key=os.environ["secret_key"], algorithm="HS256")
    return token

