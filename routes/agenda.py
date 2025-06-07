# routes/agenda.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from config.database import get_db
from controllers.agenda import obtener_agendas, crear_agenda, actualizar_agenda, eliminar_agenda, agendas_semana
from schemas.agenda import AgendaCreate, Agenda
from auth.auth_bearer import JWTBearer

router = APIRouter(tags=["Agendas"])

@router.get("/agenda", response_model=list[Agenda], dependencies=[Depends(JWTBearer())])
def listar_agendas(db: Session = Depends(get_db)):
    return obtener_agendas(db)

@router.post("/agenda", dependencies=[Depends(JWTBearer())])
def crear_nueva_agenda(agenda: AgendaCreate, db: Session = Depends(get_db)):
    return crear_agenda(db, agenda)

@router.put("/agenda/{id}", dependencies=[Depends(JWTBearer())])
def actualizar_agenda_existente(id: int, agenda: AgendaCreate, db: Session = Depends(get_db)):
    updated_agenda = actualizar_agenda(db, id, agenda)
    if not updated_agenda:
        raise HTTPException(status_code=404, detail="Agenda no encontrada")
    return {"msg": "Agenda actualizada"}

@router.delete("/agenda/{id}", dependencies=[Depends(JWTBearer(required_role="admin"))])
def eliminar_agenda_existente(id: int, db: Session = Depends(get_db)):
    success = eliminar_agenda(db, id)
    if not success:
        raise HTTPException(status_code=404, detail="Agenda no encontrada")
    return {"msg": "Agenda eliminada"}