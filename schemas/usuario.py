# schemas/usuario.py
from pydantic import BaseModel
from typing import Optional

class UsuarioBase(BaseModel):
    nombre: str
    apellido: str
    correo: str

class UsuarioCreate(UsuarioBase):
    contraseña: str

class UsuarioUpdate(UsuarioBase):
    nombre: Optional[str] = None
    apellido: Optional[str] = None
    correo: Optional[str] = None
    contraseña: Optional[str] = None

class Usuario(UsuarioBase):
    id: int
    rol: str  # Agregamos el rol al esquema de salida
    class Config:
        orm_mode = True