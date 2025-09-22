'''Cree los siguientes unit tests para el algoritmo `bubble_sort`:
    1. Funciona con una lista pequeña.
    2. Funciona con una lista grande (de más de 100 elementos.)
    3. Funciona con una lista vacía.
    4. No funciona con parámetros que no sean una lista. '''

from unit_testing import bubble_sort, ejercicio3, ejercicio4, ejercicio5, join_words, ejercicio7, EjercicioExtra1, divide, read_lines
import random
import pytest
from unittest.mock import mock_open, patch


def test_bubble_sort_with_a_small_list():
    # arrange
    input_list = [24, 0, 8, 5, 2, 4, 52, 90, 83, 5, 463]
    # act
    result = bubble_sort(input_list)
    # assert
    assert result == [0, 2, 4, 5, 5, 8, 24, 52, 83, 90, 463]


def test_bubble_sort_with_a_large_list():
    # arrange
    input_list = list(range(1, 101, 1))
    output_list = input_list
    random.shuffle(input_list)
    # act
    result = bubble_sort(input_list)
    # assert
    assert result == output_list


def test_bubble_sort_with_an_empty_list():
    # arrange
    input_list = []
    # act
    result = bubble_sort(input_list)
    # assert
    assert result == []


def test_bubble_sort_no_list_elements():
    # arrange
    input_list = 345
    # act & Assert
    with pytest.raises(TypeError):
        bubble_sort(input_list)


'''Ejercicio 2'''

'''Cree unit tests para probar 3 casos de éxito distintos de
cada uno de los ejercicios de semana 6 (exceptuando el 1 y 2).'''


'''Test Ejercicio 3'''


def test_ejercicio3_sum_list_elements_positive_numbers():
    # ararnge
    input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # Act
    result = ejercicio3(input_list)
    # assert
    assert result == 45


def test_ejercicio3_sum_list_elements_all_zeros():
    # ararnge
    input_list = [0, 0, 0, 0, 0]
    # Act
    result = ejercicio3(input_list)
    # assert
    assert result == 0


def test_ejercicio3_sum_list_elements_positive_negative_numbers():
    # ararnge
    input_list = [-2, -5, -7, 4, -99]
    # Act
    result = ejercicio3(input_list)
    # assert
    assert result == -109


'''Test Ejercicio 4'''


def test_ejercicio_4_Hola_Mundo():
    # Arrange
    test_input = 'Hola Mundo'
    # Act
    result = ejercicio4(test_input)
    # Assert
    assert result == 'odnuM aloH'


def test_ejercicio_4_KAYAK():
    # Arrange
    test_input = 'KAYAK'
    # Act
    result = ejercicio4(test_input)
    # Assert
    assert result == 'KAYAK'


def test_ejercicio_4_Desoxirribonucleico():
    # Arrange
    test_input = 'Desoxirribonucleico'
    # Act
    result = ejercicio4(test_input)
    # Assert
    assert result == 'ocielcunobirrixoseD'


'''Test Ejercicio 5'''


def test_ejercicio_5_all_upper_case():
    # Arrange
    test_input = 'ESCUELA'
    # Act
    result = ejercicio5(test_input)
    # Assert
    assert result == 'In "ESCUELA". There are 7 upper cases and 0 lower cases'


def test_ejercicio_5_all_lower_case():
    # Arrange
    test_input = 'mandarina'
    # Act
    result = ejercicio5(test_input)
    # Assert
    assert result == 'In "mandarina". There are 0 upper cases and 9 lower cases'


def test_ejercicio_5_upper_and_lower_case():
    # Arrange
    test_input = 'San Francisco'
    # Act
    result = ejercicio5(test_input)
    # Assert
    assert result == 'In "San Francisco". There are 2 upper cases and 10 lower cases'


'''Test Ejercicio 6'''


def test_ejercicio6_unsorted_words():
    # Arrange
    test_input = "python-variable-funcion-computadora-monitor"
    # Act
    result = join_words(test_input)
    # Assert
    assert result == "computadora-funcion-monitor-python-variable"


def test_ejercicio6_list_already_sorted():
    # Arrange
    test_input = "abeja-bebé-cusco-dedo-elefante"
    # Act
    result = join_words(test_input)
    # Assert
    assert result == "abeja-bebé-cusco-dedo-elefante"


def test_ejercicio6_all_the_same_word():
    # Arrange
    test_input = "KAYAK-kAYAK-Kayak-kayak"
    # Act
    result = join_words(test_input)
    # Assert
    assert result == 'KAYAK-Kayak-kAYAK-kayak'


'''Test Ejercicio 7'''


def test_ejercicio7_no_prime_numbers():
    # Arrange
    test_input = [4, 6, 8, 9, 10, 14]
    # Act
    result = ejercicio7(test_input)
    # Assert
    assert result == []


def test_ejercicio7_mixed_numbers():
    # Arrange
    test_input = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
    # Act
    result = ejercicio7(test_input)
    # Assert
    assert result == [2, 3, 5, 7, 11, 13, 17]


def test_ejercicio7_10_prime_numbers():
    # Arrange
    test_input = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
                  16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
    # Act
    result = ejercicio7(test_input)
    # Assert
    assert result == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]


'''Ejercicio Extra 1'''


def test_ejercicio_extra_1_suma_positive_numbers():
    # Arrange
    ejercicio_extra_1 = EjercicioExtra1()
    number1 = 10
    number2 = 5
    # Act
    result = ejercicio_extra_1.addition(number1, number2)
    # Assert
    assert result == 15


def test_ejercicio_extra_1_suma_negative_numbers():
    # Arrange
    ejercicio_extra_1 = EjercicioExtra1()
    number1 = -100
    number2 = -20
    # Act
    result = ejercicio_extra_1.addition(number1, number2)
    # Assert
    assert result == -120


def test_ejercicio_extra_1_suma_only_zeros():
    # Arrange
    ejercicio_extra_1 = EjercicioExtra1()
    number1 = 0
    number2 = 0
    # Act
    result = ejercicio_extra_1.addition(number1, number2)
    # Assert
    assert result == 0


def test_ejercicio_extra_1_promedio_positive_numbers():
    # Arrange
    ejercicio_extra_1 = EjercicioExtra1()
    input_list = [80, 80, 90, 90]
    # Act
    result = ejercicio_extra_1.average(input_list)
    # Assert
    assert result == 85


def test_ejercicio_extra_1_promedio_negative_numbers():
    # Arrange
    ejercicio_extra_1 = EjercicioExtra1()
    input_list = [-54, 56, -26]
    # Act
    result = ejercicio_extra_1.average(input_list)
    # Assert
    assert result == -8


def test_ejercicio_extra_1_promedio_only_zeros():
    # Arrange
    ejercicio_extra_1 = EjercicioExtra1()
    input_list = [0, 0, 0, 0, 0, 0, 0]
    # Act
    result = ejercicio_extra_1.average(input_list)
    # Assert
    assert result == 0


def test_ejercicio_extra_1_conversion_C_to_F_positive_numbers():
    # Arrange
    ejercicio_extra_1 = EjercicioExtra1()
    input_temperature = 37
    # Act
    result = ejercicio_extra_1.pass_celsius_to_fahrenheit(input_temperature)
    # Assert
    assert result == 98.60000000000001


def test_ejercicio_extra_1_conversion_C_to_F_negative_numbers():
    # Arrange
    ejercicio_extra_1 = EjercicioExtra1()
    input_temperature = 100
    # Act
    result = ejercicio_extra_1.pass_celsius_to_fahrenheit(input_temperature)
    # Assert
    assert result == 212


def test_ejercicio_extra_1_conversion_C_to_F_only_zeros():
    # Arrange
    ejercicio_extra_1 = EjercicioExtra1()
    input_temperature = 0
    # Act
    result = ejercicio_extra_1.pass_celsius_to_fahrenheit(input_temperature)
    # Assert
    assert result == 32


'''Ejercicio Extra 3'''
'''Cree un test que
- Valide que `dividir(10, 2)` retorna `5.0`
- Verifique que dividir por cero lanza un `ValueError`
- Valide que dividir con un `string` como parámetro también lanza `TypeError`
'''


def test_divide_10_2():
    # Arrange
    number_1 = 10
    number_2 = 2
    # Act
    result = divide(number_1, number_2)
    # Assert
    assert result == 5.0


def test_divide_10_0():
    # Arrange
    number_1 = 10
    number_2 = 0
    # Act & Assert
    with pytest.raises(ValueError):
        divide(number_1, number_2)


def test_divide_strings():
    # Arrange
    number_1 = 10
    number_2 = 'Mamá amaza la masa'
    # Act & Assert
    with pytest.raises(TypeError):
        divide(number_1, number_2)


'''Ejercicio Extra 4'''

'''Use `unittest.mock` para simular el contenido de un archivo
Verifique que retorna las líneas esperadas sin crear archivos reales
Compruebe que lanza `FileNotFoundError` si el archivo no existe'''


def test_read_lines_expected_lines():
    mock_file_data = "Mensajes de WhatsApp\nmostrarían cita entre Erwen Masís\ny hermano de Bulgarelli"

    with patch('builtins.open', mock_open(read_data=mock_file_data)):
        result = read_lines('fake_path.txt')
        # Comprobamos que las líneas leídas son las esperadas
        assert result == ['Mensajes de WhatsApp\n',
                          'mostrarían cita entre Erwen Masís\n', 'y hermano de Bulgarelli']


def test_read_lines_FileNotFoundError_is_launched():
    with patch('builtins.open', side_effect=FileNotFoundError):
        with pytest.raises(FileNotFoundError):
            read_lines('non_existent_file.txt')
