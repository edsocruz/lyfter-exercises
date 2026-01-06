from src.logic.category import Category
from src.data.data_counters import load_id_counters_info, save_id_counters
from datetime import datetime


class Transaction:
    '''Estos metodos deben ser llamados por separado al momento de crear el objeto y no en el constructor'''
    @staticmethod
    def get_next_id_counter():  # it returns the next id that must be used
        id_list = load_id_counters_info()
        transaction_dict = id_list[0] # Here we must know that 'Category' is the second column element in the counters file
        next_id_counter = transaction_dict["transaction"]
        return next_id_counter

    @staticmethod
    def update_current_id_counter():
        id_list = load_id_counters_info()
        transaction_dict = id_list[0]
        current_id_counter = transaction_dict["transaction"]
        transaction_dict["transaction"] = current_id_counter + 1
        save_id_counters(id_list)

    def __init__(self, id=None, type="", title="", amount=0, category=Category(), date=None):
        
        if id is not None:
            self.id = id
        else:
            self.id = self.get_next_id_counter()
            self.update_current_id_counter()

        # Validate title
        if not title.strip():
            raise ValueError("El título no puede estar vacío o contener solo espacios.")
        
        # Validate type
        if not type.strip():
            raise ValueError("El tipo no puede estar vacío o contener solo espacios.")

        # Validate amount
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError("El monto debe ser numérico y mayor que cero.")

        # Validate category
        if not category or not str(category).strip():
            raise ValueError("La categoría no puede estar vacía.")

        # Validate date
        if date is not None and isinstance(date, str):
            try:
                date = datetime.strptime(date, "%d/%m/%Y").date()
            except ValueError:
                raise ValueError("La fecha debe tener el formato DD-MM-YYYY.")

        self.type = type
        self.title = title
        self.amount = amount 
        self.category = category
        self.date = date



