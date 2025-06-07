# routes/auth.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.usuario import Usuario
from schemas.usuario import UsuarioCreate
from auth.jwt_handler import create_access_token
from config.database import get_db
from controllers.usuario import get_usuario_by_correo

router = APIRouter(tags=["Autenticación"])

@router.post("/login")
def login(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    db_usuario = get_usuario_by_correo(db, correo=usuario.correo)
    if not db_usuario or db_usuario.contraseña != usuario.contraseña:
        raise HTTPException(status_code=401, detail="Credenciales inválidas")

    access_token = create_access_token(
    data={"id": db_usuario.id, "email": db_usuario.correo, "rol": db_usuario.rol}
    )
    return {"access_token": access_token, "token_type": "bearer"}
    
