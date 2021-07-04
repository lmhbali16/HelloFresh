# HelloFresh

This is an attempt of the HelloFresh Graduate Software Engineering coding assignment. For the task click [here](https://github.com/hello-abhishek/hf-take-home-programming-challenges). This repository contains the backend part of the assignment.


## Stack

* Docker
* Python FastAPI
* Postgres
* PGAdmin
* SQLAlchemy
* Python JWT


## Database Design

For ORM design go to design [page](/design.md)

## Testing

Basic testing of endpoints and CRUD were done with Postman and Pytest respectively.

### Unit test

This is a demonstration of some testcases with pytest.

To run unit tests:

1. run docker-compose file

2. go to api folder with Terminal

3. install requirements from requirement file

```
pip install -r requirements.txt
```

4. run test_main.py file

```
pytest test_main.py
```

### Postman endpoint tests

Note: you can also test it by opening the OpenAPI feature.




## Running

PgAdmin: http://localhost:5050

 * password: admin
 * username: admin@admin.com

Server: http://localhost:8000

OpenAPI: http://localhost:8000/api/a/docs

Postgres: postgresql://postgres:postgres@postgres:5432/postgres

* username: postgres
* password: postgres

