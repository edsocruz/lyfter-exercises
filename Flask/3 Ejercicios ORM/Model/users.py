from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from Model.base import Base


#https://docs.sqlalchemy.org/en/21/orm/mapping_styles.html

#Usuarios 
# - ID
# - Nombre
# - Correo

class User(Base):
    __tablename__ = "users"
    #Note: dentro de Mapped[tipo de dato] se especifica el tipo de dato python a utilizar (int, str, float, bool, date, datetime) 
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    email: Mapped[str] = mapped_column(String(30))

    #En este punto hace falta definir las relaciones usando el ORM, esto con el Relationship() y el Back_populates
    #Un usuario va a tener una lista de de direcciones y una lista de los carros de los que es dueño
    cars: Mapped[list["Car"]] = relationship("Car", back_populates="owner")
    addresses: Mapped[list["Address"]] = relationship("Address", back_populates="user")

