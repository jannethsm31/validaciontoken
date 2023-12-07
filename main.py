from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPBasic, HTTPBasicCredentials
from fastapi.security import HTTPAuthorizationCredentials
from fastapi.middleware.cors import CORSMiddleware
import hashlib
import sqlite3
import threading
import time
import secrets
from datetime import datetime, timedelta

security_basic = HTTPBasic()
security_bearer = HTTPBearer()

app = FastAPI()

# Utiliza un pool de conexiones para manejar conexiones separadas por hilo
conn_pool = threading.local()

origins = [
    "http://localhost:8080",
    "http://172.0.0.0:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

def get_conn():
    # Crea una nueva conexión si no existe en el hilo actual
    if not hasattr(conn_pool, 'conn'):
        conn_pool.conn = sqlite3.connect('contactos.db')
    return conn_pool.conn

def create_token():
    return secrets.token_urlsafe(16)

def update_token(email):
    new_token = create_token()
    expiration_time = int(time.time()) + 600  # 10 minutos de duración
    c = get_conn().cursor()
    c.execute("UPDATE usuarios SET token = ?, expiration_time = ? WHERE username = ?", (new_token, expiration_time, email))
    get_conn().commit()
    return new_token, expiration_time

@app.get('/')
def root(credentials: HTTPAuthorizationCredentials = Depends(security_bearer)):
    token = credentials.credentials
    print(token)
    c = get_conn().cursor()

    c.execute("SELECT token, expiration_time FROM usuarios WHERE token = ?", (token,))
    response = c.fetchone()
    if not response or (response and response[1] is not None and response[1] < int(time.time())):
        return {"message": "Acceso denegado"}
    return {"message": "Acceso permitido"}

# Cada que el usuario se loggea, cambia el token
@app.get("/token/")
async def validate_user(credentials: HTTPBasicCredentials = Depends(security_basic)):
    email = credentials.username
    password_hash = hashlib.md5(credentials.password.encode()).hexdigest()
    c = get_conn().cursor()
    c.execute("SELECT token, expiration_time FROM usuarios WHERE username = ? AND password = ?", (email, password_hash))
    response = c.fetchone()
    if not response:
        raise HTTPException(status_code=401, detail="Credenciales inválidas")

    new_token, expiration_time = update_token(email)

    return {"token": new_token, "expiration_time": expiration_time}


'''
# por tiempo (600s)
@app.get("/token/")
async def validate_user(credentials: HTTPBasicCredentials = Depends(security_basic)):
    email = credentials.username
    password_hash = hashlib.md5(credentials.password.encode()).hexdigest()
    c = get_conn().cursor()
    c.execute("SELECT token, expiration_time FROM usuarios WHERE username = ? AND password = ?", (email, password_hash))
    response = c.fetchone()
    if not response:
        raise HTTPException(status_code=401, detail="Credenciales inválidas")

    current_time = datetime.utcnow()  # Obtiene la hora actual en formato UTC

    # Si el token ha expirado, actualiza el token y su expiración
    if response and response[1] is not None and response[1] < int(current_time.timestamp()):
        new_token, expiration_time = update_token(email)
        return {"token": new_token, "expiration_time": expiration_time}

    return {"token": response[0], "expiration_time": response[1]}
'''