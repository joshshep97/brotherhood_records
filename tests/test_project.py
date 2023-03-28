def test_index(client):
    response = client.get('/products/')
    assert b'<h1>Brotherhood Records</h1>' in response.data
    assert response.status_code == 200