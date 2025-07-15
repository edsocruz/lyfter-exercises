# 3. Cree una clase de `User` que:
#    Tenga un atributo de `date_of_birth`.
#    Tenga un property de `age`.
# Luego cree un decorador para funciones que acepten un `User` como parámetro
# que se encargue de revisar si el `User` es mayor de edad y arroje una excepción de no ser así.

from datetime import date


class User:
    def __init__(self, date_of_birth):
        self.date_of_birth = date_of_birth

    @property
    def age(self):
        today = date.today()
        return (today.year - self.date_of_birth.year - ((today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day)))


def is_user_of_legal_age(func):
    legal_age = 21

    def wrapper(User):
        if (User.age >= legal_age):
            result = func(User)
            print(f'User is over {legal_age}, user`s an adult')
        else:
            raise ValueError(f'User is under {legal_age}')
        return result
    return wrapper


@is_user_of_legal_age
def get_user_status(User):
    print('User age: ', User.age)


print('--------------Edso-------------------')
edso = User(date(1999, 9, 23))
print("Edso's age: ", edso.age)
try:
    get_user_status(edso)
except ValueError as ex:
    print(ex)

print('-------------------------------------')

print('\n--------------Maria-------------------')
maria = User(date(2005, 1, 1))
try:
    get_user_status(maria)
except ValueError as ex:
    print(ex)
print('--------------------------------------')
