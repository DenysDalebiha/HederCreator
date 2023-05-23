# coding: windows-1251
import csv
import ModulTable as Cap


def row_transformer(line: list, size_limit) -> list:
        for i, v in enumerate(line):

        if len(v) <= size_limit:
            print(v)
        else:
            print(v.split())


with open('data.csv', 'r') as file:
    all_data = csv.reader(file, delimiter=';')
    for row in all_data:
        print('1', row)
        ZN = row.pop(0)
        FN = row.pop(0)
        row_transformer(row, Cap.size(ZN))

