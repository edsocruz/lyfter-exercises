class RentRepository:
    def __init__(self, db_manager):
        self.db_manager = db_manager

    def _format_rents(self, user_car_record):
        return {
            "id": user_car_record[0],
            "id_user": user_car_record[1],
            "id_car": user_car_record[2],
            "return_date": f"{user_car_record[3].month}/{user_car_record[3].day}/{user_car_record[3].year}",
            "rental_status": user_car_record[4],
        }

    def create(self, id_user, id_car, return_date, rental_status):
        #possible states (active / completed)
        try:
            rent_created = self.db_manager.execute_query(
                "insert into lyfter_car_rental.Users_Cars(id_user, id_car, return_date, rental_status) VALUES (%s, %s, %s, %s) returning id, id_user, id_car, return_date, rental_status",
                (id_user, id_car, return_date, rental_status),
            )
            print("Rent inserted successfully")
            formatted_results = [self._format_rents(rent_created) for rent_created in rent_created]
            return formatted_results
        except Exception as error:
            print("Error inserting a rent into the database: ", error)
            return False

    def get_all(self):
        try:
            results = self.db_manager.execute_query(
                "SELECT id, id_user, id_car, return_date, rental_status FROM lyfter_car_rental.Users_Cars order by id ASC;"
            )
            print(results)
            formatted_results = [self._format_rents(result) for result in results]
            return formatted_results
        except Exception as error:
            print("Error getting all rents from the database: ", error)
            return False

    def get_by_id(self, _id):
        try:
            results = self.db_manager.execute_query(
                "SELECT id, id_user, id_car, return_date, rental_status FROM lyfter_car_rental.Users_Cars WHERE id = %s;",
                (_id,),
            )
            formatted_result = self._format_rents(results[0])
            return formatted_result
        except Exception as error:
            print("Error getting a rent from the database: ", error)
            return False

    def update(self, _id, id_user, id_car, return_date, rental_status):
        try:
            rent_updated = self.db_manager.execute_query(
                "UPDATE lyfter_car_rental.Users_Cars SET (id_user, id_car, return_date, rental_status) = (%s, %s, %s, %s) WHERE ID = %s returning id, id_user, id_car, return_date, rental_status",
                (id_user, id_car, return_date, rental_status, _id),
            )
            print("Rent updated successfully")
            formatted_results = [self._format_rents(rent_updated) for rent_updated in rent_updated]
            return formatted_results
        except Exception as error:
            print("Error updating a rent from the database: ", error)
            return False

#    def delete(self, _id):
#        try:
#            self.db_manager.execute_query(
#                "DELETE FROM lyfter_car_rental.Users_Cars WHERE id = (%s)", (_id,)
#            )
#            print("Rent deleted successfully")
#            return True
#        except Exception as error:
#            print("Error deleting a rent from the database: ", error)
#            return False
#        

