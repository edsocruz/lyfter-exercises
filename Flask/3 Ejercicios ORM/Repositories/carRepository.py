from Model.cars import Car
from Model.users import User
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
            owner = user
        )
        self.session.add(car)
        self.session.commit()
        return car
    
    def update(self, id,plate,brand,model,year,user):
        car = self.session.get(Car, id)
        if car is None:
            return None
        else:
            car.id = id
            car.plate = plate
            car.brand = brand
            car.model = model
            car.year = year
            car.owner = user
            self.session.commit()
            return car

    def link_user(self, car_id,user):
        car = self.session.get(Car, car_id)
        
        if car is None or user is None:
            return None
        
        car.owner = user
        self.session.commit()
        return car
    
    def select(self):
        query = select(Car).order_by(Car.id.asc())
        cars = self.session.scalars(query).all()
        return cars
    
    def delete(self, car_id):
        car = self.session.get(Car, car_id)
        if car is None:
            print("El recurso solicitado no existe en el sistema")
            return None
        else:
            self.session.delete(car)
            self.session.commit()
            return car

    
    def get(self, car_id):
        car = self.session.get(Car, car_id)
        return car