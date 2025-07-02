
class Person():
    def __init__(self, name):
        self.name = name
        self.age = 0


class Bus:
    def __init__(self, max_passengers = 0):
        self.max_passengers = max_passengers
        self.passengers_count = 0
        self.passengers = []

    def add_passenger(self, person: Person):
        status_message = ''
        if self.max_passengers > self.passengers_count:
            self.passengers.append(person)
            status_message = f'{person.name} se subió al bus'
            self.passengers_count = self.passengers_count + 1
        else:
            status_message = f'No se puede subir a {person.name}, el bus está lleno'
        return status_message

    def remove_passenger(self, person_name):
        status_message = ''
        if len(self.passengers) == 0:
            status_message = 'El bus se ya encuentra vacio' 
        for index, passenger in enumerate(self.passengers):
            if passenger.name == person_name:
                status_message = f'{person_name} se bajó del bus'
                self.passengers.pop(index)
                break
            else:
                status_message = f'No se ha encontrado a {person_name}!'
        return status_message
    
    def show_passengers(self):
        print('Lista de pasajeros:')
        for passenger in self.passengers:
            print(f'  {passenger.name}')

person_1 = Person('Edso')
person_2 = Person('Samy')
person_3 = Person('Sonia')
person_4 = Person('Edgar')
person_5 = Person('Luz')

bus_1 = Bus(4)

print('\nBus capacity: ',bus_1.max_passengers)

print(bus_1.add_passenger(person_1))
print(bus_1.add_passenger(person_2))
print(bus_1.add_passenger(person_3))
print(bus_1.add_passenger(person_4))
print(bus_1.add_passenger(person_5))
print('\n')

bus_1.show_passengers()
print('\n')

print(bus_1.remove_passenger('Luz'))
print(bus_1.remove_passenger('Edso'))
print(bus_1.remove_passenger('Sonia'))
print(bus_1.remove_passenger('Samy'))
print(bus_1.remove_passenger('Edgar'))
print(bus_1.remove_passenger('Edso'))
