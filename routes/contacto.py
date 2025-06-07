# routes/contacto.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas.contacto import ContactoCreate, Contacto
from controllers.contacto import create_contacto, get_contactos
from config.database import get_db
from auth.auth_bearer import JWTBearer

router = APIRouter(tags=["Contactos"])

@router.post("/contactos/", response_model=Contacto)
def crear_mensaje(contacto: ContactoCreate, db: Session = Depends(get_db)):
    return create_contacto(db, contacto)

@router.get("/contactos/", response_model=list[Contacto])
def listar_mensajes(db: Session = Depends(get_db)):
    return get_contactos(db)
