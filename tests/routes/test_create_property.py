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


def test_invalid_x_by_minimum_value(client):
    json = {  
        "x":-1,
        "y":750,
        "title":"title",
        "price":1250000,
        "description":"description",
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
        "title":"title",
        "price":1250000,
        "description":"description",
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
    pass

def test_invalid_y_by_maximum_value(client):
    pass   

def test_invalid_beds(client):
    pass

def test_invalid_baths(client):
    pass

def test_invalid_squareMeters(client):
    pass

def test_invalid_squareMeters(client):
    pass