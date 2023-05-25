# coding: windows-1251
import csv
import ModulTable as Cap
from random import randint
import logging

logging.basicConfig(filename='log.log', level=logging.Info)


def line_spliter(line: str) -> list:
    split_line = line.replace(',', ',^').split('^')
    if len(split_line) == 1:
        split_line = line.replace(' ', ' ^').split()
        if len(split_line) == 1:
            logging.error("unsplittable string")
    return split_line


def line_cuter(line: list, limit=5) -> list:
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


def write_to_file(factory_number: str, fiscal_number: str, cap: list, offset=0) -> None:
    """write one cap to file"""
    with open('OutData.txt', 'w') as out_file:
        out_file.write(f'%Oper($$Data,"{factory_number}",10,$$Flag)\n%If ($$Flag == 1)\n%Then\n')
        out_file.write(f'%Set $$FN = "{fiscal_number}"')
        for i, item in enumerate(cap):
            out_file.write(f'22000000;{i};{item};0;')
        out_file.write('%Else\n%EndIf\n')


if __name__ == '__main__':
    with open('data.csv', 'r') as file:
        all_data = csv.reader(file, delimiter=';')
        for row in all_data:
            print(row)
            ZN = row.pop(0)
            FN = row.pop(0)

