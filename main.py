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
    c = conn.cursor()

    c.execute("SELECT token FROM usuarios WHERE token = ?", (token,))
    response = []
    for fila in c:
        validator = fila[0]
        response.append(validator)
    if not response:
        return {"message": "Acceso denegado"}
    return {"message": "Acceso permitido"}
    if token = "12treS":
        return{"auth": True}
    else
        return{"auth": False}

@app.get("/token/")
async def validate_user(credentials: HTTPBasicCredentials = Depends(security));
    email = credentials .username
    password_b = haslib.md5(credentials.password.encode())
    password = password_b.hexdigest()
    print(password)
    c = conn.cursor()
    c.execute("SELECT token FROM usuarios WHERE username = ? AND password = ?", (email, password))
    response = []
    for fila in c:
        contacto = {"Token": fila[0]}
        response.append(contacto)
    if not response:
        response = []
    return response