
from src.logic.transaction import Transaction
from src.logic.category import Category
from src.data.data_transaction import convert_from_object_to_dictionary_transaction, convert_from_dictionary_to_object_transaction

def test_convert_from_object_to_dictionary_category():
    # arrange
    list_of_transactions = [Transaction(1,'Income','Pasteles',10000,Category('Casa'),'23/09/2025'), Transaction(2,'Spend','Gasolina',20000,Category('Transporte'),'29/09/2025')]
    result = [{'id': 1, 'type': 'Income', 'title': 'Pasteles','amount': 10000, 'category': 'Casa', 'date': '23/09/2025'},
                {'id': 2, 'type': 'Spend', 'title': 'Gasolina','amount': 20000, 'category': 'Transporte', 'date': '29/09/2025'}]
    # act
    dictionary_list = convert_from_object_to_dictionary_transaction(list_of_transactions)
    # assert
    assert dictionary_list == result

def test_convert_from_dictionary_to_object_category():
    # arrange
    list_of_dict = [{'id': 1, 'type': 'Income', 'title': 'Pasteles','amount': 10000, 'category': 'Casa', 'date': '23/09/2025'},
                {'id': 2, 'type': 'Spend', 'title': 'Gasolina','amount': 20000, 'category': 'Transporte', 'date': '29/09/2025'}]
    result = [Transaction(1,'Income','Pasteles',10000,Category('Casa'),'23/09/2025'), Transaction(2,'Spend','Gasolina',20000,Category('Transporte'),'29/09/2025')]
    # act
    object_list = convert_from_dictionary_to_object_transaction(list_of_dict)
    # assert
    for index, item in enumerate(result):
        assert item.id == object_list[index].id
        assert item.type == object_list[index].type
        assert item.title == object_list[index].title
        assert item.amount == object_list[index].amount
        assert item.category.name == object_list[index].category.name
        assert item.date == object_list[index].date
    
