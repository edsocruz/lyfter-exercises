from Model.users import User
from sqlalchemy import select

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
