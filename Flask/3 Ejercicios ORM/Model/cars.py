from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from Model.base import Base

#Automoviles
# - ID
# - Matricula
# - Marca
# - Modelo
# - Año
# - Propietario (FK)

class Car(Base):
    __tablename__ = "cars"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    plate: Mapped[str] = mapped_column(String(6))
    brand: Mapped[str] = mapped_column(String(15))
    model: Mapped[str] = mapped_column(String(15))
    year: Mapped[int] = mapped_column(Integer)
    user_id: Mapped[int | None] = mapped_column( ForeignKey("users.id")) # añadiendo el | None, le decimos que podemos esperar un null (None) como tipo de dato