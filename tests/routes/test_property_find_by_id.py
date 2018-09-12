def test_inexistent_property(client):
    id = 892829
    response = client.get('/properties/{}'.format(id))
    json = {
    "message": "Property id {} not found".format(id)
    }
    assert json == response.get_json()
    assert 404 == response.status_code