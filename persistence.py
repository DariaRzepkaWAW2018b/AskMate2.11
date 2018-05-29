import csv

def import_data_from_file(file_name):
    list_of_dict = []
    with open(file_name, 'r') as csv_file:
        csv_reader=csv.DictReader(csv_file)

        for row in csv_reader:
            list_of_dict.append(row)
        return list_of_dict


def export_data_to_file(file_name):
    with open(file_name, 'r') as csv_file:
        csv_reader=csv.DictReader(csv_file)
        with open(file_name, 'w') as new_file:
            fieldnames = create_list_of_headers(list)
            csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter=',')
            csv_writer.writeheader()
            


with open('new_test.csv', 'w') as new_file:
        fieldnames = ['Stock','Price','Quantity']
        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames,delimiter=',')

        csv_writer.writeheader()

        #for line in csv_reader:
         #   csv_writer.writerow(line)
