def test_with_success(client):
    """
    Verifica se um imóvel foi cadastrado com sucesso. Asserções:
    - Response é um json?
    - Existe um id?
    - Imóvel possui uma lista de províncias?
    - Imóvel está localizado em 1 ou 2 províncias?
    - Status HTTP é 201?
    """
    json = {  
        "x":500,
        "y":750,
        "title":"Imóvel novo x500, y750",
        "price":1250000,
        "description":"Imóvel novo x500, y750 description",
        "beds":4,
        "baths":2,
        "squareMeters":110
    }
    
    response = client.post('/properties', json=json)

    assert True == response.is_json
    response_body = response.get_json()
    assert True == (response_body['id'])
    assert list == (type(response_body['provinces']))
    assert 1 <= (len(response_body['provinces'])) <= 2
    assert 201 == response.status_code

def test_invalid_mime_type(client):
    payload = "payload"
    
    response = client.post('/properties')
    assert True == response.is_json
    response_body = response.get_json()
    assert response_body == {'message': 'Mime type is not valid'}
    assert 415 == response.status_code

def test_with_success_with_minimum_values(client):
    json = {  
        "x":0,
        "y":0,
        "title":"Imóvel novo x500, y750",
        "price":1250000,
        "description":"Imóvel novo x500, y750 description",
        "beds":1,
        "baths":1,
        "squareMeters":20
    }
    
    response = client.post('/properties', json=json)

    assert True == response.is_json
    response_body = response.get_json()
    assert True == (response_body['id'])
    assert list == (type(response_body['provinces']))
    assert 1 <= (len(response_body['provinces'])) <= 2
    assert 201 == response.status_code

def test_with_success_with_maximum_values(client):
    json = {  
        "x":1400,
        "y":1000,
        "title":"Property title",
        "price":1250000,
        "description":"Property description",
        "beds":5,
        "baths":4,
        "squareMeters":240
    }
    
    response = client.post('/properties', json=json)

    assert True == response.is_json
    response_body = response.get_json()
    assert True == (response_body['id'])
    assert list == (type(response_body['provinces']))
    assert 1 <= (len(response_body['provinces'])) <= 2
    assert 201 == response.status_code

def test_invalid_x_by_minimum_value(client):
    json = {  
        "x":-1,
        "y":750,
        "title":"Property title",
        "price":1250000,
        "description":"Property description",
        "beds":4,
        "baths":2,
        "squareMeters":110
    }

    json_error = {
        "errors": [
            {
                "field": "x",
                "message": "-1 is less than the minimum of 0"
            }
        ]
    }
    
    response = client.post('/properties', json=json)
    assert True == response.is_json
    response_body = response.get_json()
    assert json_error == response_body
    assert 422 == response.status_code


def test_invalid_x_by_maximum_value(client):
    json = {  
        "x":1401,
        "y":750,
        "title":"Property title",
        "price":1250000,
        "description":"Property description",
        "beds":4,
        "baths":2,
        "squareMeters":110
    }

    json_error = {
        "errors": [
            {
                "field": "x",
                "message": "1401 is greater than the maximum of 1400"
            }
        ]
    }
    
    response = client.post('/properties', json=json)
    assert True == response.is_json
    response_body = response.get_json()
    assert json_error == response_body
    assert 422 == response.status_code
    

def test_invalid_y_by_minimum_value(client):
    json = {  
        "x":100,
        "y":-1,
        "title":"Property title",
        "price":1250000,
        "description":"Property description",
        "beds":4,
        "baths":2,
        "squareMeters":110
    }

    json_error = {
        "errors": [
            {
                "field": "y",
                "message": "-1 is less than the minimum of 0"
            }
        ]
    }
    
    response = client.post('/properties', json=json)
    assert True == response.is_json
    response_body = response.get_json()
    assert json_error == response_body
    assert 422 == response.status_code

def test_invalid_y_by_maximum_value(client):
    json = {  
        "x":100,
        "y":1001,
        "title":"Property title",
        "price":1250000,
        "description":"Property description",
        "beds":4,
        "baths":2,
        "squareMeters":110
    }

    json_error = {
        "errors": [
            {
                "field": "y",
                "message": "1001 is greater than the maximum of 1000"
            }
        ]
    }
    
    response = client.post('/properties', json=json)
    assert True == response.is_json
    response_body = response.get_json()
    assert json_error == response_body
    assert 422 == response.status_code

def test_invalid_beds_by_minimum_value(client):
    json = {  
        "x":100,
        "y":100,
        "title":"Property title",
        "price":1250000,
        "description":"Property description",
        "beds":0,
        "baths":2,
        "squareMeters":110
    }

    json_error = {
        "errors": [
            {
                "field": "beds",
                "message": "0 is less than the minimum of 1"
            }
        ]
    }
    
    response = client.post('/properties', json=json)
    assert True == response.is_json
    response_body = response.get_json()
    assert json_error == response_body
    assert 422 == response.status_code

def test_invalid_beds_by_maximum_value(client):
    json = {  
        "x":100,
        "y":100,
        "title":"Property title",
        "price":1250000,
        "description":"Property description",
        "beds":6,
        "baths":2,
        "squareMeters":110
    }

    json_error = {
        "errors": [
            {
                "field": "beds",
                "message": "6 is greater than the maximum of 5"
            }
        ]
    }
    
    response = client.post('/properties', json=json)
    assert True == response.is_json
    response_body = response.get_json()
    assert json_error == response_body
    assert 422 == response.status_code  

def test_invalid_baths_by_minimum_value(client):
    json = {  
        "x":100,
        "y":100,
        "title":"Property title",
        "price":1250000,
        "description":"Property description",
        "beds":2,
        "baths":0,
        "squareMeters":110
    }

    json_error = {
        "errors": [
            {
                "field": "baths",
                "message": "0 is less than the minimum of 1"
            }
        ]
    }
    
    response = client.post('/properties', json=json)
    assert True == response.is_json
    response_body = response.get_json()
    assert json_error == response_body
    assert 422 == response.status_code

def test_invalid_baths_by_maximum_value(client):
    json = {  
        "x":100,
        "y":100,
        "title":"Property title",
        "price":1250000,
        "description":"Property description",
        "beds":2,
        "baths":5,
        "squareMeters":110
    }

    json_error = {
        "errors": [
            {
                "field": "baths",
                "message": "5 is greater than the maximum of 4"
            }
        ]
    }
    
    response = client.post('/properties', json=json)
    assert True == response.is_json
    response_body = response.get_json()
    assert json_error == response_body
    assert 422 == response.status_code  

def test_invalid_squareMeters(client):
    json = {  
        "x":100,
        "y":100,
        "title":"Property title",
        "price":1250000,
        "description":"Property description",
        "beds":2,
        "baths":2,
        "squareMeters":19
    }

    json_error = {
        "errors": [
            {
                "field": "squareMeters",
                "message": "19 is less than the minimum of 20"
            }
        ]
    }
    
    response = client.post('/properties', json=json)
    assert True == response.is_json
    response_body = response.get_json()
    assert json_error == response_body
    assert 422 == response.status_code

def test_invalid_squareMeters(client):
    json = {  
        "x":100,
        "y":100,
        "title":"Property title",
        "price":1250000,
        "description":"Property description",
        "beds":2,
        "baths":2,
        "squareMeters":241
    }

    json_error = {
        "errors": [
            {
                "field": "squareMeters",
                "message": "241 is greater than the maximum of 240"
            }
        ]
    }
    
    response = client.post('/properties', json=json)
    assert True == response.is_json
    response_body = response.get_json()
    assert json_error == response_body
    assert 422 == response.status_code 