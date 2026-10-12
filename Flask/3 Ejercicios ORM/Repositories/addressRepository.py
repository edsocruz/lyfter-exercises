from Model.addresses import Address
from sqlalchemy import select

class AddressRepository: 
    def __init__(self, session):
        self.session = session

    def create(self, address, user):
        address_obj = Address(
            address = address,
            user_id = user.id
        )
        self.session.add(address_obj)
        self.session.commit()
        return user

    def update(self, address_id, new_address, new_user_id):
        address_obj = self.session.get(Address, address_id)
        address_obj.address = new_address
        address_obj.user_id = new_user_id
        self.session.commit()
        return address_obj

    def select(self):
        query = select(Address).order_by(Address.id.asc())
        addresses = self.session.scalars(query).all()
        return addresses

    def delete(self, address_id):
        address = self.session.get(Address, address_id)
        if address:
            deleted_address = self.session.delete(address)
            self.session.commit()
            return deleted_address
        else:
            return "El recurso solicitado no exite en el sistema"
    

