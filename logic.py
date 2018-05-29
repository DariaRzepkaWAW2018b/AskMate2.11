#import persistance.py


def delete (list, _id):
#    import_data_from_file(list):
    for dict in list:        
        if dict['id'] == _id:
            list.remove(dict)
#            export_data_to_file(list):

