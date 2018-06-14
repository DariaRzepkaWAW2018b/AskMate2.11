import database_common
from psycopg2 import sql 



@database_common.connection_handler
def import_data_from_file_question(cursor):
    cursor.execute("SELECT * FROM question")
    # cursor.execute(
    # sql.SQL("SELECT * FROM db_table VALUES (%s)"
    #     .format(sql.Identifier("db_table"), db_table))
    list_of_dict = cursor.fetchall()
    return(list_of_dict)

@database_common.connection_handler
def add_data_question(cursor, new_title, new_message, new_image=None):
    cursor.execute("INSERT into question (title, message, image) VALUES (%s, %s, %s)", 
    (new_title, new_message, new_image))
#queti$

@database_common.connection_handler
def import_data_from_file_answer(cursor, id_q):
    cursor.execute("SELECT * FROM answer WHERE question_id = (%s)", (id_q,))
    list_of_dict = cursor.fetchall()
    return list_of_dict

@database_common.connection_handler
def add_data_answer(cursor, new_message):
    cursor.execute("INSERT into answer (message) VALUES (%s)", (new_message,))
    print("1")

#answer#
@database_common.connection_handler
def import_data_from_file_comment(cursor):
    cursor.execute("SELECT * FROM comment")
    list_of_dict = cursor.fetchall()
    return list_of_dict



@database_common.connection_handler
def add_data_comment(cursor, new_message):
    cursor.execute("INSERT into comment (message) VALUES (%s)",(new_message,))


