# controllers/contacto.py
from sqlalchemy.orm import Session
from models.contacto import Contacto
from schemas.contacto import ContactoCreate

# Crear un nuevo mensaje/reseña
def create_contacto(db: Session, contacto: ContactoCreate):
    db_contacto = Contacto(**contacto.dict())
    db.add(db_contacto)
    db.commit()
    db.refresh(db_contacto)
    return db_contacto

# Obtener todos los mensajes/reseñas
def get_contactos(db: Session):
    return db.query(Contacto).all()