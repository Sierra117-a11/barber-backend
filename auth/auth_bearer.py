#auth/auth_bearer.py
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from typing import Optional
from auth.jwt_handler import verify_token, TokenData

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/login")

class JWTBearer:
    def __init__(self, required_role: Optional[str] = None):
        self.required_role = required_role

    async def __call__(self, token: str = Depends(oauth2_scheme)) -> TokenData:
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="No se pudieron validar las credenciales",
            headers={"WWW-Authenticate": "Bearer"},
        )
        token_data = verify_token(token, credentials_exception)

        if self.required_role and token_data.rol != self.required_role:
            raise HTTPException(status_code=403, detail="Permiso denegado: rol insuficiente")
        
        return token_data