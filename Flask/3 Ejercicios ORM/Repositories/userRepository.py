from Model.users import User
from Model.cars import Car
from sqlalchemy import select, func

class UserRepository: 
    def __init__(self, session):
        self.session = session

    def create(self, name, email):
        user = User(
            name = name,
            email = email
        )
        self.session.add(user)
        self.session.commit()
        return user

    def update(self, user_id, new_name, new_email):
        user = self.session.get(User, user_id)

        if user is None or new_name is None or new_email is None:
            return None
        else:        
            user.name = new_name
            user.email = new_email
            self.session.commit()
            return user

    def select(self):
        query = select(User).order_by(User.id.asc())
        users = self.session.scalars(query).all()
        return users

    def select_users_with_more_than_one_car(self):
        query = select(User).join(User.cars).group_by(User.id).having(func.count(Car.id) > 1).order_by(User.id.asc())
        users_with_more_than_one_car = self.session.scalars(query).all()
        return users_with_more_than_one_car

    def select_all_addresses_and_cars_of_user(self, user_id):
        user = self.session.get(User, user_id)
        if user is None:
            return None
        else:
            addresses = user.addresses
            cars = user.cars
            return addresses, cars

    def delete(self, user_id):
        user = self.session.get(User, user_id)
        if user is None:
            print("El recurso solicitado no existe en el sistema")
            return None
        else:
            self.session.delete(user)
            self.session.commit()
            return user
    
    def get(self, user_id):
        user = self.session.get(User, user_id)
        return user
