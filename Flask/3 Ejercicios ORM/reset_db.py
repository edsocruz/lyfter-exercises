from sqlalchemy import create_engine

from Model.base import Base
from Model.users import User
from Model.cars import Car
from Model.addresses import Address

DB_URI = "postgresql://postgres:postgres@localhost:5432/postgres"
engine = create_engine(DB_URI, echo=True)

# Eliminar las tablas existentes
Base.metadata.drop_all(engine)

# Crear las tablas nuevamente
Base.metadata.create_all(engine)

print("Tablas recreadas correctamente")