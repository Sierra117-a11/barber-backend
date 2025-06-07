# main.py
from fastapi import FastAPI
from config.database import engine, Base
from routes.usuario import router as usuario_router
from routes.contacto import router as contacto_router
from routes.agenda import router as agenda_router
from routes.auth import router as auth_router
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.utils import get_openapi
from fastapi.openapi.docs import get_swagger_ui_html  

app = FastAPI(
    title="API de Barbería",
    description="Gestión de usuarios, agenda, contactos y autenticación",
    version="1.0.0"
)

@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)

app.include_router(usuario_router, prefix="/api")
app.include_router(contacto_router, prefix="/api")
app.include_router(agenda_router, prefix="/api")
app.include_router(auth_router, prefix="/api")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# === CONFIGURACIÓN PERSONALIZADA DE SWAGGER PARA USAR JWT ===

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title=app.title,
        version=app.version,
        description=app.description,
        routes=app.routes,
    )

    # Agregar esquema de seguridad con Bearer Token
    openapi_schema["components"]["securitySchemes"] = {
        "BearerAuth": {
            "type": "http",
            "scheme": "bearer",
            "bearerFormat": "JWT",
            "description": "Introduce tu token JWT en el formato: `Bearer <tu_token>`"
        }
    }

    openapi_schema["security"] = [{"BearerAuth": []}]
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi


@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui():
    return get_swagger_ui_html(
        openapi_url="/openapi.json",
        title="API de Barbería - Documentación",
        swagger_js_url="https://cdn.jsdelivr.net/npm/swagger-ui-dist @5/swagger-ui-bundle.js",
        swagger_css_url="https://cdn.jsdelivr.net/npm/swagger-ui-dist @5/swagger-ui.css",
    )


@app.get("/")
def read_root():
    return {"message": "Bienvenido a la API de Barbería"}