# config/database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Configuración de la base de datos SIN CONTRASEÑA
#DATABASE_URL = "mysql+pymysql://root@localhost/python" 
 
DATABASE_URL = "mysql://root:HjAifvyKXDoKXamMpiAcVNhcSzFsBMCF@maglev.proxy.rlwy.net:54052/railway"  

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Función para obtener una sesión de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
