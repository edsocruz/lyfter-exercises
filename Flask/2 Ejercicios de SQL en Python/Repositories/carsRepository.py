class CarsRepository:
    def __init__(self, db_manager):
        self.db_manager = db_manager

    def _format_car(self, car_record):
        return {
            "id": car_record[0],
            "brand": car_record[1],
            "model": car_record[2],
            "production_year": car_record[3],
            "status": car_record[4],
        }
    

    def create(self, brand, model, production_year, status):
        try:
            #possible states (maintenance/unavailable -> available -> rented)
            result = self.db_manager.execute_query(
                "INSERT INTO lyfter_car_rental.Cars (brand, model, production_year, status) VALUES (%s, %s, %s, %s) returning id, brand, model, production_year, status",
                (brand, model, production_year, status),
            )
            print("Car inserted successfully")
            return result
        except Exception as error:
            print("Error inserting a car into the database: ", error)
            return False

    def get_all(self):
        try:
            results = self.db_manager.execute_query(
                "SELECT id, brand, model, production_year, status FROM lyfter_car_rental.Cars order by id ASC;"
            )
            formatted_results = [self._format_car(result) for result in results]
            return formatted_results
        except Exception as error:
            print("Error getting all Cars from the database: ", error)
            return False

    def get_by_id(self, _id):
        try:
            results = self.db_manager.execute_query(
                "SELECT id, brand, model, production_year, status FROM lyfter_car_rental.Cars WHERE id = %s;",
                (_id,),
            )
            formatted_result = self._format_car(results[0])
            return formatted_result
        except Exception as error:
            print("Error getting a car from the database: ", error)
            return False

    def update(self, _id, brand, model, production_year, status):
        try:
            result = self.db_manager.execute_query(
                "UPDATE lyfter_car_rental.Cars SET (brand, model, production_year, status) = (%s, %s, %s,%s) WHERE ID = %s returning id, brand, model, production_year, status" ,
                (brand, model, production_year, status, _id),
            )
            print("Car updated successfully")
            return result
        except Exception as error:
            print("Error updating a car from the database: ", error)
            return False

#    def delete(self, _id):
#        try:
#            self.db_manager.execute_query(
#                "DELETE FROM lyfter_car_rental.Cars WHERE id = (%s)", (_id,)
#            )
#            print("Car deleted successfully")
#            return True
#        except Exception as error:
#            print("Error deleting a car from the database: ", error)
#            return False


