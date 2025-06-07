# schemas/contacto.py
from pydantic import BaseModel
from datetime import datetime

class ContactoBase(BaseModel):
    nombre: str
    correo: str
    mensaje: str

class ContactoCreate(ContactoBase):
    pass

class Contacto(ContactoBase):
    id: int
    fecha_contacto: datetime

    class Config:
        orm_mode = True