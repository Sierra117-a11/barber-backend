# models/agenda.py
from sqlalchemy import Column, Integer, String, Date, DateTime
from config.database import Base

class Agenda(Base):
    __tablename__ = "agenda"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nombre_completo = Column(String(255), nullable=False)
    celular = Column(String(15), nullable=False)
    edad = Column(Integer, nullable=False)
    correo = Column(String(255), nullable=False)
    fecha_solicitud = Column(Date, nullable=False)
    fecha_hora_agenda = Column(DateTime, nullable=False)
    tipo_corte = Column(String(100), nullable=False)
