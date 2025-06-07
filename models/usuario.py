# models/usuario.py
from sqlalchemy import Column, Integer, String, DateTime, Enum
from sqlalchemy.sql import func
from config.database import Base
import enum

class RolEnum(str, enum.Enum):
    admin = "admin"
    cliente = "cliente"

class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nombre = Column(String(50), nullable=False)
    apellido = Column(String(50), nullable=False)
    correo = Column(String(100), unique=True, nullable=False)
    contraseña = Column(String(100), nullable=False)
    rol = Column(Enum(RolEnum), default=RolEnum.cliente, nullable=False)  # Nuevo campo
    fecha_registro = Column(DateTime(timezone=True), server_default=func.now())