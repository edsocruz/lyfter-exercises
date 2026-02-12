import pytest
import os
import csv
from src.logic.category import Category
from src.data.data_category import convert_from_object_to_dictionary_category, convert_from_dictionary_to_object_category, save_categories_info

def test_convert_from_object_to_dictionary_category_category():
    # arrange
    list_of_categories = [Category('Salud'),Category('Comida'),Category('Ocio'),Category('Transporte')]
    # act
    dictionary_list = convert_from_object_to_dictionary_category(list_of_categories)
    result = [{'category': 'Salud' },{'category':'Comida'  },{'category': 'Ocio' },{'category': 'Transporte' }]
    # assert
    assert dictionary_list == result

def test_convert_from_dictionary_to_object_category_category():
    # arrange
    list_of_dict = [{'category': 'Salud' },{'category':'Comida'  },{'category': 'Ocio' },{'category': 'Transporte' }]
    result = ['Salud','Comida','Ocio','Transporte']
    # act
    object_list = convert_from_dictionary_to_object_category(list_of_dict)
    # assert
    for index, item in enumerate(result):
        assert item == object_list[index].name
    

