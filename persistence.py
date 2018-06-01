import csv
import time

def import_headers_from_file(file_name):
    with open(file_name, 'r') as csv_file:
        csv_reader=csv.reader(csv_file)

        for line in csv_reader:
            return line




def import_data_from_file(file_name):
    list_of_dict = []
    with open(file_name, 'r') as csv_file:
        csv_reader=csv.DictReader(csv_file)

        for row in csv_reader:
            a = float(row["submisson_time"])
            row["submisson_time"] = time.ctime(a)
            list_of_dict.append(row)
        return list_of_dict


def export_data_to_file(path, data):
    with open(path, 'w') as csv_file:
        writer = csv.writer(csv_file, delimeter='_')
        for line in data:
            writer.writerow(line)
            
        
    return
            
