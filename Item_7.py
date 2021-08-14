import csv


def import_csv():

    file_path = input('Input file path: ')
    with open(file_path) as file:
        data_file = csv.reader(file)
        csv_key = next(data_file)
        print([dict(zip(csv_key,x)) for x in data_file])


dict_CSV()
