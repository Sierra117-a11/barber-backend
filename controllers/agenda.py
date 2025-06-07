from sqlalchemy.orm import Session
from models.agenda import Agenda  # ✅ Usamos el modelo SQLAlchemy real
from schemas.agenda import AgendaCreate, AgendaUpdate  # ✅ Solo esquemas Pydantic
from datetime import datetime, timedelta

def obtener_agendas(db: Session):
    return db.query(Agenda).all()

def crear_agenda(db: Session, agenda: AgendaCreate):
    db_agenda = Agenda(**agenda.dict())  # ✅ Agenda es el modelo SQLAlchemy
    db.add(db_agenda)
    db.commit()
    db.refresh(db_agenda)
    return db_agenda

def actualizar_agenda(db: Session, agenda_id: int, agenda_data: AgendaUpdate):
    db_agenda = db.query(Agenda).filter(Agenda.id == agenda_id).first()
    if not db_agenda:
        return None
    for key, value in agenda_data.dict(exclude_unset=True).items():
        setattr(db_agenda, key, value)
    db.commit()
    db.refresh(db_agenda)
    return db_agenda

def eliminar_agenda(db: Session, agenda_id: int):
    db_agenda = db.query(Agenda).filter(Agenda.id == agenda_id).first()
    if not db_agenda:
        return None
    db.delete(db_agenda)
    db.commit()
    return True

def agendas_semana(db: Session):
    hoy = datetime.today()
    fin = hoy + timedelta(days=7)
    return db.query(Agenda).filter(Agenda.fecha_hora_agenda.between(hoy, fin)).all()

