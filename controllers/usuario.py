#controllers/usuario.py
from sqlalchemy.orm import Session
from models.usuario import Usuario
from schemas.usuario import UsuarioCreate, UsuarioUpdate


def get_usuario_by_correo(db: Session, correo: str):
    return db.query(Usuario).filter(Usuario.correo == correo).first()


def create_usuario(db: Session, usuario: UsuarioCreate):
    db_usuario = Usuario(**usuario.dict())
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario

def get_usuarios(db: Session):
    return db.query(Usuario).all()

def get_usuario_by_id(db: Session, usuario_id: int):
    return db.query(Usuario).filter(Usuario.id == usuario_id).first()

# 👇 Esta es la función que faltaba
def get_usuario_by_email(db: Session, correo: str):
    return db.query(Usuario).filter(Usuario.correo == correo).first()

def update_usuario(db: Session, usuario_id: int, usuario_data: UsuarioUpdate):
    db_usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()
    if not db_usuario:
        return None
    for key, value in usuario_data.dict(exclude_unset=True).items():
        setattr(db_usuario, key, value)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario

def delete_usuario(db: Session, usuario_id: int):
    db_usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()
    if not db_usuario:
        return None
    db.delete(db_usuario)
    db.commit()
    return True