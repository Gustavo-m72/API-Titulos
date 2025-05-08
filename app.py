from fastapi import FastAPI
from http import HTTPStatus
from schemas import *

app = FastAPI() 

@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():    
    return {'message': 'teste'}

