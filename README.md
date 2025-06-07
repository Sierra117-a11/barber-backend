# Proyecto: El Arte del Barbero - Backend y Frontend

## Descripción
Este es un sistema web Full Stack para la gestión de citas, usuarios y mensajes de contacto para una barbería. Implementa autenticación JWT, roles de usuario (admin/cliente), y funciones CRUD para agendas, usuarios y comentarios.

## Tecnologías utilizadas

### Backend (FastAPI):
- **FastAPI**
- **SQLAlchemy**
- **MySQL** (o MariaDB)
- **PyMySQL**
- **python-jose** (para manejo de JWT)
- **Uvicorn** (como servidor ASGI)

### Frontend:
- **HTML/CSS**
- **JavaScript** (vanilla)
- **Bootstrap 5**
- **Axios**

## Estructura del Proyecto

```
proyecto_barberia/
│
├── backend/
│   ├── auth/
│   │   ├── __init__.py
│   │   ├── auth_bearer.py
│   │   └── jwt_handler.py
│   ├── config/
│   │   └── database.py
│   ├── controllers/
│   │   ├── agenda.py
│   │   ├── contacto.py
│   │   └── usuario.py
│   ├── models/
│   │   ├── agenda.py
│   │   ├── contacto.py
│   │   └── usuario.py
│   ├── routes/
│   │   ├── agenda.py
│   │   ├── auth.py
│   │   ├── contacto.py
│   │   └── usuario.py
│   ├── schemas/
│   │   ├── agenda.py
│   │   ├── contacto.py
│   │   └── usuario.py
│   └── main.py
│
├── frontend/
│   ├── agendar.html
│   ├── contacto.html
│   ├── configurar-usuario.html
│   ├── cortes-y-estilos.html
│   ├── quienes-somos.html
│   ├── index.html
│   ├── estilos.css
│   └── validacion.js
│
├── requirements.txt
└── README.md
```

## Instalación y ejecución

1. Clonar el repositorio:
```bash
git clone https://github.com/tu_usuario/arte-barbero.git
cd arte-barbero/backend
```

2. Instalar dependencias:
```bash
pip install -r requirements.txt
```

3. Configurar base de datos en `config/database.py` y crearla desde MySQL.

4. Ejecutar el servidor:
```bash
uvicorn main:app --reload
```

## Endpoints importantes

### Autenticación
- POST `/api/login`

### Usuarios
- GET `/api/usuarios/` (solo admin)
- GET `/api/usuarios/buscar?correo=...` ( admin/usuario)
- POST `/api/usuarios/` (registro sin JWT)
- PUT `/api/usuarios/{id}` ( admin/usuario)
- DELETE `/api/usuarios/{id}` ( admin/usuario)

### Agenda
- GET `/api/agenda` 
- POST `/api/agenda` ( admin/usuario)
- PUT `/api/agenda/{id}` ( admin/usuario)
- DELETE `/api/agenda/{id}` (solo admin)

### Contacto
- GET `/api/contacto` ( admin/usuario)
- POST `/api/contacto` ( admin/usuario)

## Consulta SQL para insertar un usuario administrador

```sql
INSERT INTO usuario (nombre, apellido, correo, contraseña, rol, fecha_registro)
VALUES ('Admin', 'Barbero', 'admin@example.com', 'admin123', 'admin', NOW());
```

## Cambios recientes incluidos
- 🔐 Validación de roles en rutas protegidas.
- 🔑 Autenticación JWT completa (login y verificación en frontend).
- 📋 CRUD de contacto (comentarios y sugerencias).
- 👤 Página de configuración de perfil (actualizar datos/eliminar cuenta).
- 👁️ Control de visibilidad de botones y secciones por rol (admin/cliente).
- 💡 Cierre de sesión automático con botón desde frontend.

---

## Autoría
José Camargo, Germán Gutiérrez, Julián Venegas y Víctor Yepéz — 2025
