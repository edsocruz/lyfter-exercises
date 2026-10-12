from Model.cars import Car
from sqlalchemy import select

class CarRepository:
    def __init__(self, session):
            self.session = session
    
    def create(self, plate, brand, model, year, user=None):
        car = Car(
            plate = plate,
            brand = brand,
            model = model,
            year = year, 
            user_id = user
        )
        self.session.add(car)
        self.session.commit()
        return car
    
    def update(self, id,plate,brand,model,year,user_id):
        car = self.session.get(Car, id)
        car.id = id
        car.plate = plate
        car.brand = brand
        car.model = model
        car.year = year
        car.user_id = user_id
        self.session.commit()
        return car

    def link_a_user(self, id,user_id):
        car = self.session.get(Car, id)
        car.user_id = user_id
        self.session.commit()
        return car
    
    def select(self):
        query = select(Car).order_by(Car.id.asc())
        cars = self.session.scalars(query).all()
        return cars
    
    def delete(self, car_id):
        car = self.session.get(Car, car_id)
        if car:
            deleted_car = self.session.delete(car)
            self.session.commit()
            return deleted_car
        else: 
            return "El recurso solicitado no existe en el sistema"
    
    def get(self, car_id):
        car = self.session.get(Car, car_id)
        return car