from fastapi import FastAPI
from fastapi.requests import Request
import socket
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()


@app.get('/')
def index(request: Request):
    client_ip = request.client.host
    return (f'Server ip is {socket.gethostbyname(socket.gethostname())} and client ip is {client_ip}. '
            f'Also user from environment: {os.getenv("MY_ENV")}')
