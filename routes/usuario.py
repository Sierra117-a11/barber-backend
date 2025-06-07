#routes/usuario.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from config.database import get_db
from controllers.usuario import create_usuario, delete_usuario, get_usuarios, update_usuario, get_usuario_by_email
from schemas.usuario import UsuarioCreate, UsuarioUpdate, Usuario
from auth.auth_bearer import JWTBearer, TokenData


router = APIRouter(tags=["Usuarios"])

# ✅ Crear usuario — SIN protección JWT
@router.post("/usuarios/", response_model=Usuario)
def crear_usuario(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    return create_usuario(db, usuario)

# ✅ Solo admin puede listar todos los usuarios
@router.get("/usuarios/", response_model=list[Usuario], dependencies=[Depends(JWTBearer(required_role="admin"))])
def listar_todos_los_usuarios(db: Session = Depends(get_db)):
    return get_usuarios(db)

# ✅ Cliente puede buscar SU PROPIO perfil por correo
@router.get("/usuarios/buscar", response_model=Usuario, dependencies=[Depends(JWTBearer())])
def buscar_usuario_por_correo(
    correo: str,
    db: Session = Depends(get_db),
    current_user: TokenData = Depends(JWTBearer())
):
    usuario = get_usuario_by_email(db, correo)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    
    # Cliente solo puede acceder a sus propios datos
    if current_user.rol != "admin" and usuario.id != current_user.id:
        raise HTTPException(status_code=403, detail="No tienes permiso para ver este usuario")
    return usuario

# ✅ Cliente puede actualizar SU CUENTA
@router.put("/usuarios/{usuario_id}", response_model=Usuario, dependencies=[Depends(JWTBearer())])
def actualizar_usuario(
    usuario_id: int,
    usuario_data: UsuarioUpdate,
    db: Session = Depends(get_db),
    current_user: TokenData = Depends(JWTBearer())
):
    if current_user.rol != "admin" and current_user.id != usuario_id:
        raise HTTPException(status_code=403, detail="No puedes editar otra cuenta")
    
    updated_usuario = update_usuario(db, usuario_id, usuario_data)
    if not updated_usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return updated_usuario

# ✅ Cliente puede eliminar SU CUENTA
@router.delete("/usuarios/{usuario_id}", response_model=dict, dependencies=[Depends(JWTBearer())])
def eliminar_usuario(
    usuario_id: int,
    db: Session = Depends(get_db),
    current_user: TokenData = Depends(JWTBearer())
):
    if current_user.rol != "admin" and current_user.id != usuario_id:
        raise HTTPException(status_code=403, detail="No puedes eliminar otra cuenta")
    
    success = delete_usuario(db, usuario_id)
    if not success:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return {"detail": "Usuario eliminado correctamente"}