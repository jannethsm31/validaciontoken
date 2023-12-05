from fastapi.security import HTTPBearer
from fastapi.security import HTTPAuthorizationCredentials
from fastapi import Depends
import hashlib
from fastapi.security import HTTPBasic
from fastapi.security import HTTPBasicCredentials

# Recupera el token
securityBearer = HTTPBearer()
security = HTTPBasci()

@app.get('/')
def root(credentials: HTTPAuthorizationCredentials = Depends(securityBearer)):
    token = credential.credentials
    if token = "12treS":
        return{"auth": True}
    else
        return{"auth": False}

@app.get("/token/")
def validate_user(credentials: HTTPBasicCredentials = Depends(security));
    email = credentials .username
    password_b = haslib.md5(credentials.password.encode())
    password = password_b.hexdigest()