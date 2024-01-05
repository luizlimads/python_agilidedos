class TestRouterUser:
	def test_access_blank_route(self, client):
		response = client.get('/')
		assert response.status_code == 302
		assert response.location in "/login"

	def test_access_login(self, client):
		response = client.get('/login')
		assert response.status_code == 200

	def test_access_register(self, client):
		response = client.get('/register')
		assert response.status_code == 200
