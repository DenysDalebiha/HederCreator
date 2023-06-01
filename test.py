# coding: windows-1251
import csv
import ModulTable as Cap
from random import randint
import logging

logging.basicConfig(level=logging.INFO)


def str_spliter(line: str) -> list:
    """ return split line
    >>>str_spliter("КИЇВСЬКИЙ ЗООЛОГІЧНИЙ ПАРК ЗАГАЛЬНОДЕРЖАВНОГО ЗНАЧЕННЯ")
    ['КИЇВСЬКИЙ ', 'ЗООЛОГІЧНИЙ ', 'ПАРК ', 'ЗАГАЛЬНОДЕРЖАВНОГО ', 'ЗНАЧЕННЯ']
    >>>str_spliter('м. Київ, Шевченківський р-он, Проспект Перемоги, буд. 32')
    ['м. Київ,', ' Шевченківський р-он,', ' Проспект Перемоги,', ' буд. 32']
    """
    split_str = line.replace(',', ',^').split('^')
    if len(split_str) == 1:
        split_str = line.replace(' ', ' ^').split('^')
        if len(split_str) == 1:
            logging.error("unsplittable string")
    return split_str


def line_cuter(line: list, limit=32) -> list:
    """check len(item) < limit else - cut"""
    out_l = []
    while line:
        if len(line[0]) > limit:
            big = line.pop(0)
            line = str_spliter(big) + line
        out_l.append(line.pop(0))
    logging.debug(f'{line} ->\n->{out_l}')
    return out_l


def grupator(line, limit=32) -> str:
    """return one element of cap
    """
    if line:
        if len(line) == 1:
            return line
        out = line.pop(0)
        if Cap.check_markers(out):
            out = out.center(limit)
        while len(out) + len(line[0]) <= limit:
            out += line.pop(0)
            if len(line) == 0:
                break
        return out.center(limit).rstrip()
    else:
        logging.error("Empty line")


def write_to_file(factory_number: str, fiscal_number: str, cap: list, offset=0) -> None:
    """write one cap to file"""
    with open('OutData.txt', 'w') as out_file:
        out_file.write(f'%Oper($$Data,"{factory_number}",10,$$Flag)\n%If ($$Flag == 1)\n%Then\n')
        out_file.write(f'%Set $$FN = "{fiscal_number}"')
        for i, item in enumerate(cap):
            out_file.write(f'22000000;{i};{item};0;')
        out_file.write('%Else\n%EndIf\n')
    logging.info(f'{cap} write to file')


if __name__ == '__main__':
    with open('data.csv', 'r') as file:
        all_data = csv.reader(file, delimiter=';')
        for row in all_data:
            ZN = row.pop(0)
            FN = row.pop(0)
            while row:
                print(grupator(line_cuter(row)))
