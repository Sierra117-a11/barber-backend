# schemas/agenda.py
from pydantic import BaseModel
from typing import Optional
from datetime import date, datetime

class AgendaBase(BaseModel):
    nombre_completo: str
    celular: str
    edad: int
    correo: str
    fecha_solicitud: date
    fecha_hora_agenda: datetime
    tipo_corte: str

class AgendaCreate(AgendaBase):
    pass

class AgendaUpdate(BaseModel):
    nombre_completo: Optional[str] = None
    celular: Optional[str] = None
    edad: Optional[int] = None
    correo: Optional[str] = None
    fecha_solicitud: Optional[date] = None
    fecha_hora_agenda: Optional[datetime] = None
    tipo_corte: Optional[str] = None

class Agenda(AgendaBase):
    id: int

    class Config:
        orm_mode = True
