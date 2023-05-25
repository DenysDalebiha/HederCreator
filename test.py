# coding: windows-1251
import csv
import ModulTable as Cap
from random import randint


def row_transformer(line: list, size_limit) -> list:
    for i, v in enumerate(line):
        print(i, v)
        if len(v) <= size_limit:
            print(v)
        else:
            print(v.split())


# with open('data.csv', 'r') as file:
#     all_data = csv.reader(file, delimiter=';')
#     for row in all_data:
#         print('1', row)
#         ZN = row.pop(0)
#         FN = row.pop(0)
#         row_transformer(row, Cap.size(ZN))

def line_cuter(line:list, limit = 5)->list:
    """check item < limit else - cut"""
    out_l = []
    while line:
        if line[0] > limit:
            big = line.pop(0)
            line.insert(0, big - limit)
            out_l.append(limit)
            print(line)
        else:
            out_l.append(line.pop(0))
    return out_l
def groupator(line, limit = 7)-> list:
    """return one element of cap"""
    if len(line) == 1:
        return line
    out = [line.pop(0)]
    while sum(out) + line[0] <= limit:
        out.append(line.pop(0))
        if len(line) == 0:
            break
    print (out)
    return out


if __name__ == '__main__':
    #in_line = [randint(1, 5) for i in range(20)]
    in_line = [15, 1, 2, 6]
    print(in_line)
    print(line_cuter(in_line,4))
    # out_line = []
    # while len(in_line) > 0:
    #     out_line.append(groupator(in_line, 10))
    # print(out_line)
