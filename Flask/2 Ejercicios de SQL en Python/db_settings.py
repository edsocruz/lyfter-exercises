import psycopg2


class PgManager:

    def __init__(self, db_name, user, password, host, port=5432):
        self.db_name = db_name
        self.user = user
        self.password = password
        self.host = host
        self.port = port
#Cambié la configuracion anterior en la que tenía un metodo de create connection, excecute query y close connection; por una en donde se abra y se cierre automaticamente la conexion a la hora de hacer cada consulta a la DB 
    def execute_query(self, query, params=None): # acá cambié el *args por un parametro normal ya que a la hora de usar este metodo, lo que se manda despues del query es una tupla, si dejo el *args tendría una tupla dentro de una tupla  

        connection = psycopg2.connect(
            dbname=self.db_name,
            user=self.user,
            password=self.password,
            host=self.host,
            port=self.port
        )
        cursor = connection.cursor()
        try:
            cursor.execute(query, params)
            if cursor.description:
                result = cursor.fetchall()
            else:
                result = None
            connection.commit()
            return result
        except Exception:
            connection.rollback()
            raise
        finally:
            cursor.close()
            connection.close()


