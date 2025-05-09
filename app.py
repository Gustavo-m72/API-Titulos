from http import HTTPStatus

from fastapi import FastAPI

from schemas import Message, User

app = FastAPI()


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'teste'}


@app.post('/user/', status_code=HTTPStatus.CREATED, response_model=User)
def create_user(user: User):
    return user
