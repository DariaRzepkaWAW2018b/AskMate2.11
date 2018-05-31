import persistence
import itertools

def find_by_id_q(id):
    list = persistence.import_data_from_file("sample_data/question.csv")
    for item in list:
        for k, v in item.items():
            if k == 'id' and v == id:
                title_of_question = item[' title']
    return title_of_question

def find_by_id_a(id):
    list_of_answer = persistence.import_data_from_file("sample_data/answer.csv")
    list_of_dictionaries =[]
    for item in list_of_answer:
        if item['question_id'] == id:
            list_of_dictionaries.append(item)
    return list_of_dictionaries
    

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

def create_new_id(qa, _question_id= None):
    _id=[]
    if qa == "q":
        data = persistence.import_data_from_file("sample_data/question.csv")
        for dict in data:
            _id.append(dict['id'])
    if qa == 'a':
        data = persistence.import_data_from_file("sample_data/answer.csv")
        for dict in data:
            if dict['question_id']== str(_question_id):
                _id.append(dict['id'])
    new_id= int(max(_id))
    return new_id +1

def create_dict(list_of_data):
    header = persistence.import_headers_from_file('sample_data/question.csv')
    new_post={}
    post=[]
    new_post = dict(itertools.zip_longest(header, list_of_data, fillvalue=None))
    return new_post
