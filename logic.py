import persistence.py


def delete_by_id(qa, id):
    '''
    Deletes post by id
    Args:
        qa - str q or a, q for question, a for answer
        id - str or int - id of element to delete
    '''
    if qa == "q":
        data = persistence.import_data_from_file("sample_data/question.csv")
    if qa == "a":
        data = persistence.import_data_from_file("sample_data/answer.csv")
    id_index_number = None
    for counter, entry in enumerate(data):
        if str(entry['id']) == str(id):
            id_index_number = counter
    del data[id_index_number]
    if qa == "q":
        persistence.export_data_to_file("sample_data/question.csv", data)
    if qa == "a":
        persistence.export_data_to_file("sample_data/answer.csv", data)
