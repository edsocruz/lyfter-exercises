from Model.addresses import Address
from Model.users import User
from sqlalchemy import select

class AddressRepository: 
    def __init__(self, session):
        self.session = session

    def create(self, address, user):
        address_obj = Address(
            address = address,
            user = user
        )
        self.session.add(address_obj)
        self.session.commit()
        return address_obj

    def update(self, address_id, new_address, new_user):
        address_obj = self.session.get(Address, address_id)
        
        if address_obj is None or new_user is None:
            return None
        else:
            address_obj.address = new_address
            address_obj.user = new_user
            self.session.commit()
            return address_obj

    def select(self):
        query = select(Address).order_by(Address.id.asc())
        addresses = self.session.scalars(query).all()
        return addresses

    def delete(self, address_id):
        address = self.session.get(Address, address_id)
        if address is None:
            return "El recurso solicitado no exite en el sistema"
        else:
            self.session.delete(address)
            self.session.commit()
            return address
            

