

# Stotippos

Implementação do Desafio de Backend para o [Grupo Zap](https://github.com/grupozap/code-challenge/)

# 1. Ambiente local

## 1.1 Executando localmente

Instalar as dependências no seu venv:

 ```
 pip install -r requirements.txt 
 ```

 Criar banco sqlite local:

 Entrar no REPL do python
 ```
 python
 ```
Importar os módulos abaixo e executar comando de criação do banco

```
from app import db, create_app
```
```
db.create_all(app=create_app())
```

O banco **properties.db (sqlite)** será criado na pasta raiz

Inicializar a aplicação:

```flask run```

O serviço estará disponível em http://localhost:5000 


## 1.2 Testando localmente

Instalar as dependências no seu venv:

 ```
 pip install -r requirements.txt 
 ```

 Executar os testes:

 ```
 pytest -v
 ```


# 2. API 

- Descrição da API:
    - Criar Imovel em Stotippos
    - Buscar Imóvel em Stotippos
    - Buscar Imóveis em uma área de Stotippos
 
 Resource      | Descrição                       |
|:--------------|:----------------------------------|
|POST  `/properties`      | Cria um imóvel novo em Stotippos
|GET  `/properties/{id}`    | Retorna um imóvel cadastrado em Stotippos
|GET  `/properties?ax={ax}&ay={ay}&bx={bx}&by={by}` | Retorna uma lista de imóveis de uma área de Stotippos

Observações:
- Para as operações de busca, quando resultados não são encontrados a API retorna status HTTP 404.
- Parâmetros de payload ou de url com valores não permitidos retornam status HTTP 422.


## 2.1 Criar imóvel em Stotippos

Ao criar um imóvel com sucesso, a API retorna status HTTP 201.

**Request:**

Payload em Json:

```
{  
   "x":500,
   "y":750,
   "title":"Imóvel novo x500, y750",
   "price":1250000,
   "description":"Imóvel novo x500, y750 description",
   "beds":4,
   "baths":2,
   "squareMeters":110
}
```

**Response:**

O response da operação  possui todos os atributos enviados no payload, complementados com o id do imóvel, e a lista de províncias de Stotippos onde o mesmo se encontra.

```
{
    "baths": 2,
    "beds": 4,
    "description": "Imóvel novo x500, y750 description",
    "id": 23,
    "price": 1250000,
    "provinces": [
        "Gode",
        "Ruja"
    ],
    "squareMeters": 110,
    "title": "Imóvel novo x500, y750",
    "x": 500,
    "y": 750
}
```

### Validações

Caso os dados dos parâmetros não respeitem os valores aceitos, a API retorna **status HTTP 422** com a lista dos erros encontrados no response, conforme exemplo:

**Request com X maior do que 1400 e Y maior que 1000:**

```
{  
   "x":1401,
   "y":2750,
   "title":"Imóvel novo x500, y750",
   "price":1250000,
   "description":"Imóvel novo x500, y750 description",
   "beds":4,
   "baths":2,
   "squareMeters":110
}
```


**Response:**

```
{
    "errors": [
        {
            "field": "x",
            "message": "1401 is greater than the maximum of 1400"
        },
        {
            "field": "y",
            "message": "2750 is greater than the maximum of 1000"
        }
    ]
}
```


## 2.2 Buscar Imóvel

Ao buscar um imóvel existente, a API retorna status HTTP 200.

**Request :**
```
curl -X GET #{BASE_URL}/properties/3 
```
**Response:**

```
{
    "baths": 2,
    "beds": 4,
    "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
    "id": 3,
    "price": 1250000,
    "provinces": [
        "Scavy"
    ],
    "squareMeters": 110,
    "title": "Imóvel código 1, com 5 quartos e 4 banheiros",
    "x": 100,
    "y": 344
}
```
### Validações

Ao tentar recuperar um imóvel cujo ID é inexistente, a API retorna status HTTP 404, conforme exemplo:

**Request com ID inexistente:**

```
curl -X GET #{BASE_URL}/properties/99912 
```

**Response:**

```
{
    "message": "Property id 99912 not found"
}
```


## 2.3 Buscar Imóveis em uma área de Stotippos

Ao conseguir buscar imóveis na área desejada, a API retorna status HTTP 200.

**Request**
```
curl -X GET '#{BASE_URL}/properties?ax=1200&ay=800&bx=1400&by=20' 
```  
**Response**
```
{
    "foundProperties": 2,
    "properties": [
        {
            "id": 26,
            "x": 1201,
            "y": 750,
            "title": "Imóvel novo x500, y750",
            "price": 1250000,
            "description": "Imóvel novo x500, y750 description",
            "beds": 4,
            "baths": 2,
            "squareMeters": 110,
            "provinces": [
                "Jaby"
            ]
        },
        {
            "id": 27,
            "x": 1400,
            "y": 750,
            "title": "Imóvel novo x500, y750",
            "price": 1250000,
            "description": "Imóvel novo x500, y750 description",
            "beds": 4,
            "baths": 2,
            "squareMeters": 110,
            "provinces": [
                "Jaby"
            ]
        }
    ]
}
```

### Validações

**Cenário 1: Não há propriedades na região**

Quando não existem imóveis entre os pontos A e B, a API retorna **status HTTP 404.**


**Request**
```
curl -X GET '#{BASE_URL}/properties?ax=1200&ay=800&bx=400&by=20'
``` 

**Response**
```
{
    "message": "No properties found with these coordinates"
}
```

**Cenário 2: Quando valores dos parâmetros de URL estão fora da faixa de valores permitida**

Quando algum dos parâmetros de URL está fora dos valores aceitos, a API retorna **status HTTP 422.**


**Request**
```
curl -X GET '#{BASE_URL}/properties?ax=2200&ay=3800&bx=400&by=20'
``` 

**Response**
```
{
    "errors": [
        {
            "field": "ax",
            "message": "2200 is greater than the maximum of 1400"
        },
        {
            "field": "ay",
            "message": "3800 is greater than the maximum of 1000"
        }
    ]
}
```
# 3. Escolhas técnicas

- Flask com Blueprint para modularização
- Repository Pattern
- Validação de request com jsonschema
- SQLAlchemy para persistência de dados
- Sqlite como banco de dados
- Utilização de Status HTTP 200, 201, 404, 415, 422
- Pytest para testes

# 4. Deploy

# TODO

- Incluir mais testes
- Incluir deploy
- Incluir Lint/Coverage