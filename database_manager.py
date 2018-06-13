import database_common
from psycopg2 import sql 



@database_common.connection_handler
def import_data_from_file(cursor):
    cursor.execute("SELECT * FROM question;")
    list_of_dict = cursor.fetchall()
    return list_of_dict