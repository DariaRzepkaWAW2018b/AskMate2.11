import persistence.py


def delete_by_id(qa, id):
    '''
    Deletes post by id
    Args:
        qa - str q or a, q for question, a for answer
        id - str or int - id of element to delete
    '''
    if qa == "q":
        q_data = persistence.import_data_from_file("sample_data/question.csv")
        a_data = persistence.import_data_from_file("sample_data/answer.csv")
        id_index_number = None
        for counter, entry in enumerate(q_data):
            if str(entry['id']) == str(id):
                id_index_number = counter
        del q_data[id_index_number]
        for counter, entry in enumerate(a_data):
            if str(entry['question_id']) == str(id):
                id_index_number = counter
        del a_data[id_index_number]
            persistence.export_data_to_file("sample_data/question.csv", q_data)
            persistence.export_data_to_file("sample_data/answer.csv", a_data)
    if qa == "a":
        data = persistence.import_data_from_file("sample_data/answer.csv")
        id_index_number = None
        for counter, entry in enumerate(data):
            if str(entry['id']) == str(id):
                id_index_number = counter
        del data[id_index_number]
        persistence.export_data_to_file("sample_data/answer.csv", data)


def find_by_id(id)
    for item in list_of_dict:
        id_s = item.get("id")
        if id_s == id:
            return(item)