import json
import os

def clear(): return os.system('clear') #Esta funcion es para limpiar todo lo que hay en la consola


def read_json_file(path=''):  # acá paso de un Json a un diccionario de Python
    with open(path, 'r') as json_file:
        data = json.load(json_file)
    return data


def write_json_file(path, information):  # acá paso de un diccionario de Python a un Json
    with open(path, 'w') as json_file:
        json.dump(information, json_file)


def show_menu():
    clear()
    print('Presione "i" para introducir un pokemon nuevo')
    print('Presione "q" para salir ')


def request_pokemon_info():
    name = input('Introduzca el nombre: ')
    type = input('Introduzca el Type: ')
    hp = int(input('Introduzca el HP: '))
    attack = int(input('Introduzca Attack: '))
    defense = int(input('Introduzca el Defense: '))
    sp_attack = int(input('Introduzca el Sp. Attack: '))
    sp_defense = int(input('Introduzca Sp. Defense: '))
    speed = int(input('Introduzca el Speed: '))

    new_pokemon_dictionary = {
        "name": {
            "english": name
        },
        "type": [
            type
        ],
        "base": {
            "HP": hp,
            "Attack": attack,
            "Defense": defense,
            "Sp. Attack": sp_attack,
            "Sp. Defense": sp_defense,
            "Speed": speed
        }
    }
    return new_pokemon_dictionary


def save_pokemon_info(new_pokemon_info):
    data = []
    data = read_json_file('pokemons.json')
    data.append(new_pokemon_info)
    write_json_file('pokemons.json', data)


def control():
    user_input = ''
    while not user_input == 'q':
        show_menu()
        user_input = input('-> ')
        if user_input == 'i':
            new_pokemon_info = request_pokemon_info()
            save_pokemon_info(new_pokemon_info)
    exit()


def main():
    control()


if __name__ == '__main__':
    try:
        main()
    except Exception as ex:
        print(f'An unexpected error occurred: {ex}')
