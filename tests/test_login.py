import json

from app.model.user import User

class TestLogin:
	
    def test_login_with_valid_user(self, client):
        user_test = User(login = "valido1",password="123")
        response = client.post('/login',data=user_test.to_json())
        assert response.location in "/home"

