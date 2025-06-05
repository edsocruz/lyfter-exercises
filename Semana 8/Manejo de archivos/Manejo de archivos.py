import os
clear = lambda: os.system('clear')
clear()

def read_file(path):
    list_of_songs = []
    with open(path) as file:
        for line in file.readlines():
            #print(line)
            list_of_songs.append(line)
    return list_of_songs

def sort_songs(list_of_songs):
    generic_word = ""
    for i in range(0,len(list_of_songs)):
        for j in range(0,len(list_of_songs)-1):
            if(list_of_songs[i] < list_of_songs[j]):
                generic_word = list_of_songs[i]
                list_of_songs[i] = list_of_songs[j]
                list_of_songs[j] = generic_word
    return list_of_songs 

def save_info(path, list):
    info = ''
    for item in list:
        info = info + item
    #print(info)
    with open(path,'w', encoding='utf-8') as file:
        file.write(info)

def main():
    songs = read_file('Canciones.txt')
    sorted_songs = sort_songs(songs)
    save_info('Sorted songs.txt', sorted_songs)


    # Crear un archivo de ejemplo para demostrar seek()
    with open('example.txt', 'w') as f:
        f.write("1234567890\nABCDEFGHIJ")
    
    # Leer desde una posición específica usando seek()
    with open('example.txt', 'r') as file:
        #file.seek(5)         # Mueve el cursor 5 bytes desde el inicio
        #print(file.read(1))  # Lee 1 byte (debería imprimir '6')
    
        print(file.tell())  # Lee 1 byte (debería imprimir 'H')


if __name__ == '__main__':
    try:
        main()
    except Exception as ex:
	    print(f'An unexpected error occurred: {ex}')
