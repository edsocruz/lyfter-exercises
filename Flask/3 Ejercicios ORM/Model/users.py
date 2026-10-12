from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column
from Model.base import Base

#https://docs.sqlalchemy.org/en/21/orm/mapping_styles.html

#Usuarios 
# - ID
# - Nombre
# - Correo

class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[String] = mapped_column(String(30))
    email: Mapped[String] = mapped_column(String(30))