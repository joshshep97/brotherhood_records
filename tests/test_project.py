def test_index(client):
    response = client.get('/products/')
    assert b'<h1>Brotherhood Records</h1>' in response.data
    assert response.status_code == 200
    assert b'Login' in response.data
    assert b'Register' in response.data
    

def test_login(client):
    response = client.get('/auth/login/', data={'username': 'test', 'password': 'test'})
    assert response.status_code == 200


def test_reg(client):
    response = client.get('/auth/register/', data={'username': 'test', 'password': 'test'})
    assert response.status_code == 200
    assert b'Login' in response.data
    assert b'Register' in response.data

