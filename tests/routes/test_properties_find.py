import pytest

def create_properties(client):
    json_in_two_provinces = {  
        "x":500,
        "y":750,
        "title":"Property title",
        "price":1250000,
        "description":"Property description",
        "beds":4,
        "baths":2,
        "squareMeters":200
    }

    json_in_gode = {  
        "x":0,
        "y":1000,
        "title":"Property title",
        "price":1250000,
        "description":"Property description",
        "beds":4,
        "baths":2,
        "squareMeters":200
    }
    
    client.post('/properties', json=json_in_two_provinces)
    client.post('/properties', json=json_in_gode)


@pytest.mark.parametrize("ax,ay,bx,by", [(0,1000,1400,0)])
def test_success_search_with_results(client, ax, ay, bx, by):
    create_properties(client)
    response_success = {
        "foundProperties": 2,
        "properties": [
            {
                "id": 1,
                "x": 500,
                "y": 750,
                "title": "Property title",
                "price": 1250000,
                "description": "Property description",
                "beds": 4,
                "baths": 2,
                "squareMeters": 200,
                "provinces": [
                    "Gode",
                    "Ruja"
                ]
            },
            {
                "id": 2,
                "x": 0,
                "y": 1000,
                "title": "Property title",
                "price": 1250000,
                "description": "Property description",
                "beds": 4,
                "baths": 2,
                "squareMeters": 200,
                "provinces": [
                    "Gode"
                ]
            }
        ]
    }
    response = client.get('/properties?ax={}&ay={}&bx={}&by={}'.format(ax,ay,bx,by))
    assert True == response.is_json
    response_body = response.get_json()
    assert 2 == response_body['foundProperties']
    assert 2 == len(response_body['properties'])

    assert response.status_code == 200

@pytest.mark.parametrize("ax,ay,bx,by", [(0,0,0,0)])
def test_success_search__without_results(client, ax, ay, bx, by):
    response_without_results = {"message": "No properties found with these coordinates"}
    response = client.get('/properties?ax={}&ay={}&bx={}&by={}'.format(ax,ay,bx,by))
    assert response_without_results == response.get_json()
    assert response.status_code == 404

@pytest.mark.parametrize("ax,ay,bx,by", [(-1,-1,-1,-1)])
def test_invalid_all_params(client, ax, ay, bx, by):
    response_error = {
        "errors": [
            {
                "field": "ax",
                "message": "-1 is less than the minimum of 0"
            },
            {
                "field": "ay",
                "message": "-1 is less than the minimum of 0"
            },
            {
                "field": "bx",
                "message": "-1 is less than the minimum of 0"
            },
            {
                "field": "by",
                "message": "-1 is less than the minimum of 0"
            }
        ]
    }

    response = client.get('/properties?ax={}&ay={}&bx={}&by={}'.format(ax,ay,bx,by))
    assert response_error == response.get_json()
    assert response.status_code == 422


@pytest.mark.parametrize("ax,ay,bx,by", [(-1,0,0,0)])
def test_invalid_ax_minimum_value(client, ax, ay, bx, by):
    response_error = {
        "errors": [
            {
                "field": "ax",
                "message": "-1 is less than the minimum of 0"
            }
        ]
    }
    response = client.get('/properties?ax={}&ay={}&bx={}&by={}'.format(ax,ay,bx,by))
    assert response_error == response.get_json()
    assert response.status_code == 422


@pytest.mark.parametrize("ax,ay,bx,by", [(1401,0,0,0)])
def test_invalid_ax_maximum_value(client, ax, ay, bx, by):
    response_error = {
        "errors": [
            {
                "field": "ax",
                "message": "1401 is greater than the maximum of 1400"
            }
        ]
    }
    response = client.get('/properties?ax={}&ay={}&bx={}&by={}'.format(ax,ay,bx,by))
    assert response_error == response.get_json()
    assert response.status_code == 422


@pytest.mark.parametrize("ax,ay,bx,by", [(0,-1,0,0)])
def test_invalid_ay_minimum_value(client, ax, ay, bx, by):
    response_error = {
        "errors": [
            {
                "field": "ay",
                "message": "-1 is less than the minimum of 0"
            }
        ]
    }
    response = client.get('/properties?ax={}&ay={}&bx={}&by={}'.format(ax,ay,bx,by))
    assert response_error == response.get_json()
    assert response.status_code == 422

@pytest.mark.parametrize("ax,ay,bx,by", [(0,1001,0,0)])
def test_invalid_ay_maximum_value(client, ax, ay, bx, by):
    response_error = {
        "errors": [
            {
                "field": "ay",
                "message": "1001 is greater than the maximum of 1000"
            }
        ]
    }
    response = client.get('/properties?ax={}&ay={}&bx={}&by={}'.format(ax,ay,bx,by))
    assert response_error == response.get_json()
    assert response.status_code == 422
    pass


@pytest.mark.parametrize("ax,ay,bx,by", [(0,0,-1,0)])
def test_invalid_bx_minimum_value(client, ax, ay, bx, by):
    response_error = {
        "errors": [
            {
                "field": "bx",
                "message": "-1 is less than the minimum of 0"
            }
        ]
    }
    response = client.get('/properties?ax={}&ay={}&bx={}&by={}'.format(ax,ay,bx,by))
    assert response_error == response.get_json()
    assert response.status_code == 422
    pass

@pytest.mark.parametrize("ax,ay,bx,by", [(0,0,1401,0)])
def test_invalid_bx_maximum_value(client, ax, ay, bx, by):
    response_error = {
        "errors": [
            {
                "field": "bx",
                "message": "1401 is greater than the maximum of 1400"
            }
        ]
    }
    response = client.get('/properties?ax={}&ay={}&bx={}&by={}'.format(ax,ay,bx,by))
    assert response_error == response.get_json()
    assert response.status_code == 422
    pass


@pytest.mark.parametrize("ax,ay,bx,by", [(0,0,0,-1)])
def test_invalid_by_minimum_value(client, ax, ay, bx, by):
    response_error = {
        "errors": [
            {
                "field": "by",
                "message": "-1 is less than the minimum of 0"
            }
        ]
    }
    response = client.get('/properties?ax={}&ay={}&bx={}&by={}'.format(ax,ay,bx,by))
    assert response_error == response.get_json()
    assert response.status_code == 422
    pass

@pytest.mark.parametrize("ax,ay,bx,by", [(0,0,0,1001)])
def test_invalid_by_maximum_value(client, ax, ay, bx, by):
    response_error = {
        "errors": [
            {
                "field": "by",
                "message": "1001 is greater than the maximum of 1000"
            }
        ]
    }
    response = client.get('/properties?ax={}&ay={}&bx={}&by={}'.format(ax,ay,bx,by))
    assert response_error == response.get_json()
    assert response.status_code == 422
    pass
