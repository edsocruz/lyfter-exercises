import pytest
from src.logic.category import Category

def test_category_default_name():
    # arrange
    category_name = 'Generic Category'
    # act
    new_object_category = Category()
    # assert
    assert category_name == new_object_category.name

def test_category_custom_name():
    # arrange
    category_name = 'Cuidado personal'
    # act
    new_object_category = Category('Cuidado personal')
    # assert
    assert category_name == new_object_category.name


