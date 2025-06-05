import csv
import os
def clear(): return os.system('clear')


def save_data_using_coma(path, data, headers):
    if os.path.isfile(path):
        with open(path, 'a', encoding='utf-8', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, headers)
            writer.writerows(data)
    else:
        with open(path, 'w', encoding='utf-8', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, headers)
            writer.writeheader()
            writer.writerows(data)

# Ejercio #2


def save_data_using_tab(path, data, headers):
    if os.path.isfile(path):
        with open(path, 'a', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, headers, delimiter="\t")
            writer.writerows(data)
    else:
        with open(path, 'w', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, headers, delimiter="\t")
            writer.writeheader()
            writer.writerows(data)


def request_data():
    os.system('clear')
    nombre = input("Ingrese el nombre: ")
    genero = input("Ingrese el género: ")
    desarrollador = input("Ingrese el desarrollador: ")
    clasificacion_ESRB = input("Ingrese la clasificacion ESRB: ")
    information = [{'nombre': nombre, 'genero': genero,
                    'desarrollador': desarrollador, 'clasificacion': clasificacion_ESRB}]
    return information


def show_menu():
    print('Presione "i" para introducir un registro nuevo')
    print('Presione "n" para salir')


def control():
    video_games_headers = [
        'nombre',
        'genero',
        'desarrollador',
        'clasificacion'
    ]
    user_input = ""
    while not user_input == 'n':
        os.system('clear')
        show_menu()
        user_input = input('->')
        if user_input == 'i':
            info = request_data()
            save_data_using_coma('videogames_coma.csv', info, video_games_headers)
            save_data_using_tab('videogames_tab.csv', info, video_games_headers)


def main():
    control()


if __name__ == '__main__':
    try:
        main()
    except Exception as ex:
        print(f'An unexpected error occurred: {ex}')
