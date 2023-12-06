from fastapi.security import HTTPBearer
from fastapi.security import HTTPAuthorizationCredentials
from fastapi import Depends
import hashlib
from fastapi.security import HTTPBasic
from fastapi.security import HTTPBasicCredentials
import sqlite3

security = HTTPBasci()

# Recupera el token
securityBearer = HTTPBearer()

app = FastAPI()

conn = sqlite3.connect('sql/usuarios.db')

@app.get('/')
def root(credentials: HTTPAuthorizationCredentials = Depends(securityBearer)):
    token = credentialsv.credentials
    valor = ''
    print(token)
    if token = "12treS":
        return{"auth": True}
    else
        return{"auth": False}

@app.get("/token/")
def validate_user(credentials: HTTPBasicCredentials = Depends(security));
    email = credentials .username
    password_b = haslib.md5(credentials.password.encode())
    password = password_b.hexdigest()