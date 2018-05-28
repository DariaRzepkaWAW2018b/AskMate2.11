import csv

def import_data_from_file(file_name):
    list_of_dict = []
    with open(file_name, 'r') as csv_file:
        csv_reader=csv.DictReader(csv_file)

        for row in csv_reader:
            list_of_dict.append(row)
        return list_of_dict

print(import_data_from_file('sample_data/question.csv'))