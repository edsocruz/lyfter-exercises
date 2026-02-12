import pytest
from datetime import date
from src.logic.transaction import Transaction
from src.logic.category import Category

def test_transaction_empty_title():
    # act & assert
    with pytest.raises(ValueError) as exc_info:
        Transaction(15, 'Income', '',15000,Category('Cuidado personal'),'17/12/2025')
    assert str(exc_info.value) == "El título no puede estar vacío o contener solo espacios."

def test_transaction_empty_amount():
    # act & assert
    with pytest.raises(ValueError) as exc_info:
        Transaction(15, 'Income', 'Reembolso',None,Category('Cuidado personal'),'17/12/2025')
    assert str(exc_info.value) == "El monto debe ser numérico y mayor que cero."

def test_transaction_empty_category():
    # act & assert
    with pytest.raises(ValueError) as exc_info:
        Transaction(15, 'Income', 'Reembolso',15000,None,'17/12/2025')
    assert str(exc_info.value) == "La categoría no puede estar vacía."

def test_transaction_invalid_date():
    # act & assert
    with pytest.raises(ValueError) as exc_info:
        Transaction(15, 'Income', 'Reembolso',15000,Category('Cuidado personal'),'23-09-1999')
    assert str(exc_info.value) == "La fecha debe tener el formato DD-MM-YYYY."


def test_transaction_custom_name():
    # arrange
    transaction_type = 'Income'
    transaction_title = 'Reembolso'
    transaction_amount = 15000
    transaction_category_name = 'Cuidado personal'
    transaction_date = date(2025,12,17)
    # act
    new_object_transaction = Transaction(15, 'Income', 'Reembolso',15000,Category('Cuidado personal'),'17/12/2025')
    # assert
    assert new_object_transaction.id != None
    assert new_object_transaction.type == transaction_type
    assert new_object_transaction.title == transaction_title
    assert new_object_transaction.amount == transaction_amount
    assert transaction_category_name == new_object_transaction.category.name
    assert new_object_transaction.date == transaction_date

