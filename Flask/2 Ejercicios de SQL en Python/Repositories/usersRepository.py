class UserRepository:
    def __init__(self, db_manager):
        self.db_manager = db_manager

    def _format_user(self, user_record):
        return {
            "id": user_record[0],
            "full_name": user_record[1],
            "email": user_record[2],
            "username": user_record[3],
            "password": user_record[4],
            "birth_date": f"{user_record[5].month}/{user_record[5].day}/{user_record[5].year}",
            "account_status": user_record[6]
        }

    def create(self, full_name, email, username, password, birth_date, account_status):
        try:
            result = self.db_manager.execute_query(
                "insert into lyfter_car_rental.Users(name, email, username, password, birth_date, account_status) values (%s, %s, %s,%s, %s, %s) returning id, name, email, username, password, birth_date, account_status",
                (full_name, email, username, password, birth_date, account_status),
            )
            print("\033[32mUser inserted successfully\033[0m")
            formatted_results = [self._format_user(result) for result in result]
            return formatted_results
        except Exception as error:
            print("\033[31mError inserting a user into the database: \033[0m", error)
            return None

    def get_all(self):
        try:
            results = self.db_manager.execute_query(
                "SELECT id, name, email, username, password, birth_date, account_status FROM lyfter_car_rental.Users order by id ASC;"
            )
            formatted_results = [self._format_user(result) for result in results]
            return formatted_results
        except Exception as error:
            print("\033[31mError getting all users from the database: \033[0m", error)
            return False

    def get_by_id(self, _id):
        try:
            results = self.db_manager.execute_query(
                "select id, name, email, username, password, birth_date, account_status FROM lyfter_car_rental.Users WHERE id = %s;",
                (_id,),
            )
            formatted_result = self._format_user(results[0])
            return formatted_result
        except Exception as error:
            print(("\033[31mError getting a user from the database: \033[0m") , error)
            return None

    def update(self, _id, full_name, email, username, password, birth_date, account_status):
        try:
            data_updated = self.db_manager.execute_query(
                "UPDATE lyfter_car_rental.Users SET (name, email, username, password, birth_date, account_status) = (%s, %s, %s, %s, %s, %s) WHERE ID = %s returning id, name, email, username, password, birth_date, account_status",
                (full_name, email, username, password, birth_date, account_status, _id),
            )
            print("User updated successfully")
            return data_updated
        except Exception as error:
            print("\033[31mError updating a user from the database: \033[0m", error)
            return None

#    def delete(self, _id):
#        try:
#            self.db_manager.execute_query(
#                "DELETE FROM lyfter_car_rental.Users WHERE id = (%s)", (_id,)
#            )
#            print("User deleted successfully")
#            return True
#        except Exception as error:
#            print("\033[31mError deleting a user from the database: \033[0m", error)
#            return False


