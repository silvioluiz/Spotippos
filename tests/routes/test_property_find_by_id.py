def test_inexistent_property(client):
    id = 892829
    response = client.get('/properties/{}'.format(id))
    response_json = {
    "message": "Property id {} not found".format(id)
    }
    assert response_json == response.get_json()
    assert 404 == response.status_code

def test_existent_property(client):
    json = {  
        "x":100,
        "y":100,
        "title":"Property title",
        "price":1250000,
        "description":"Property description",
        "beds":4,
        "baths":2,
        "squareMeters":200
    }
    
    response_create = client.post('/properties', json=json)
    created_id = response_create.get_json()['id']

    response_find = client.get('/properties/{}'.format(created_id))
    
    assert True == response_find.is_json
    response_find_body = response_find.get_json()
    assert created_id == (response_find_body['id'])

    assert 100 == (response_find_body['x'])
    assert 100 == (response_find_body['y'])
    assert "Property title" == (response_find_body['title'])
    assert 1250000 == (response_find_body['price'])
    assert "Property description" == (response_find_body['description'])
    assert 4 == (response_find_body['beds'])
    assert 2 == (response_find_body['baths'])
    assert 200 == (response_find_body['squareMeters'])
    assert list == (type(response_find_body['provinces']))
    assert 1 <= (len(response_find_body['provinces'])) <= 2
    assert 200 == response_find.status_code