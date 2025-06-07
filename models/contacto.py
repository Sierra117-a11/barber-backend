# models/contacto.py
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from config.database import Base

class Contacto(Base):
    __tablename__ = "contactos"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)
    correo = Column(String(100), nullable=False)
    mensaje = Column(String(500), nullable=False)
    fecha_contacto = Column(DateTime(timezone=True), server_default=func.now())