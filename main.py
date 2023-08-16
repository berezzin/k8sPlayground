from fastapi import FastAPI
from fastapi.requests import Request
import socket

app = FastAPI()


@app.get('/')
def index(request: Request):
    client_ip = request.client.host
    return f'Server ip is {socket.gethostbyname(socket.gethostname())} and client ip is {client_ip}'
