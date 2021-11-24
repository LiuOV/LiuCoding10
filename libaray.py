import csv

def loadList(filename):
    with open(filename, newline='') as csv_file:
        reader = csv.reader(csv_file)
        datalist = list(reader)
    return datalist