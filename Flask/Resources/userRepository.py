from Flask.Resources.db_for_userRepository import PgManager

db_manager = PgManager(
    db_name="postgres",
    user="postgres",
    password="postgres",
    host="localhost"
)


class UserRepository:
    def __init__(self, db_manager):
        self.db_manager = db_manager

    def _format_user(self, user_record):
        return {
            "id": user_record[0],
            "full_name": user_record[1],
            "email": user_record[2],
            "password": user_record[3],
        }

    def create(self, full_name, email, password):
        try:
            self.db_manager.execute_query(
                "INSERT INTO lyfter_duad.users (full_name, email, password) VALUES (%s, %s, %s)",
                (full_name, email, password),
            )
            print("User inserted successfully")
            self.db_manager.close_connection()
            return True
        except Exception as error:
            print("Error inserting a user into the database: ", error)
            return False

    def get_all(self):
        try:
            results = self.db_manager.execute_query(
                "SELECT id, full_name, email, password FROM lyfter_duad.users;"
            )
            formatted_results = [self._format_user(result) for result in results]
            self.db_manager.close_connection()
            return formatted_results
        except Exception as error:
            print("Error getting all users from the database: ", error)
            return False

    def get_by_id(self, _id):
        try:
            results = self.db_manager.execute_query(
                "SELECT id, full_name, email, password FROM lyfter_duad.users WHERE id = %s;",
                (_id,),
            )
            formatted_result = self._format_user(results[0])
            self.db_manager.close_connection()
            return formatted_result
        except Exception as error:
            print("Error getting a user from the database: ", error)
            return False

    def update(self, _id, full_name, email, password):
        try:
            self.db_manager.execute_query(
                "UPDATE lyfter_duad.users SET (full_name, email, password) = (%s, %s, %s) WHERE ID = %s",
                (full_name, email, password, _id),
            )
            print("User updated successfully")
            self.db_manager.close_connection()
            return True
        except Exception as error:
            print("Error updating a user from the database: ", error)
            return False

    def delete(self, _id):
        try:
            self.db_manager.execute_query(
                "DELETE FROM lyfter_duad.users WHERE id = (%s)", (_id,)
            )
            print("User deleted successfully")
            self.db_manager.close_connection()
            return True
        except Exception as error:
            print("Error deleting a user from the database: ", error)
            return False
        

