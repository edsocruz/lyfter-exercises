import pytest
from src.logic.transaction import Transaction
from src.logic.category import Category

def test_transaction_default_name():
    # arrange
    category_name = 'Generic Category'
    # act
    new_object_transaction = Transaction()
    # assert
    assert new_object_transaction.id != None
    assert new_object_transaction.type == ""
    assert new_object_transaction.title == ""
    assert new_object_transaction.amount == 0
    assert category_name == new_object_transaction.category.name
    assert new_object_transaction.date == None

def test_transaction_custom_name():
    # arrange
    transaction_type = 'Income'
    transaction_title = 'Reembolso'
    transaction_amount = 15000
    transaction_category_name = 'Cuidado personal'
    transaction_date = '17/12/2025'
    # act
    new_object_transaction = Transaction(15, 'Income', 'Reembolso',15000,Category('Cuidado personal'),'17/12/2025')
    # assert
    assert new_object_transaction.id != None
    assert new_object_transaction.type == transaction_type
    assert new_object_transaction.title == transaction_title
    assert new_object_transaction.amount == transaction_amount
    assert transaction_category_name == new_object_transaction.category.name
    assert new_object_transaction.date == transaction_date

