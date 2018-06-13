import database_common
from psycopg2 import sql 




@database_common.connection_handler
def import_data_from_file(cursor):
    cursor.execute("SELECT * FROM question;")
    list_of_dict = cursor.fetchall()
    return list_of_dict

@database_common.connection_handler
def add_data(cursor, new_title, new_message, new_image=None):
    cursor.execute("INSERT into question (title, message, image) VALUES (%s, %s, %s)", (new_title, new_message, new_image))
    