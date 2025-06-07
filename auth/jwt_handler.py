#auth/jwt_handler.py
from datetime import datetime, timedelta
from typing import Optional
from jose import JWTError, jwt
from fastapi import HTTPException
from pydantic import BaseModel
from config.database import get_db
from models.usuario import Usuario
from sqlalchemy.orm import Session

SECRET_KEY = "5m)-3#w%p(@=h-esz()fnrmfzh$#yp2idddddsr"  # Usa la misma clave que antes
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

class TokenData(BaseModel):
    id: Optional[int] = None
    email: Optional[str] = None
    rol: Optional[str] = None


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verify_token(token: str, credentials_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("email")
        rol: str = payload.get("rol")
        id: int = payload.get("id")  # 👈 AÑADIR
        if email is None or rol is None or id is None:
            raise credentials_exception
        return TokenData(id=id, email=email, rol=rol)
    except JWTError:
        raise credentials_exception

