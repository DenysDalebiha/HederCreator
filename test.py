import csv
import ModulTable as Cap


def row_transformer(line: list) -> list:
    """ line = ['КИЇВСЬКИЙ ЗООЛОГІЧНИЙ ПАРК ЗАГАЛЬНОДЕРЖАВНОГО ЗНАЧЕННЯ', '"БIЛЕТНА КАСА"',
    'м. Київ, Шевченківський р-он, Проспект Перемоги, буд. 32']
    return ['   КИЇВСЬКИЙ ЗООЛОГІЧНИЙ ПАРК   ', '   ЗАГАЛЬНОДЕРЖАВНОГО ЗНАЧЕННЯ   ',
      '      "БIЛЕТНА КАСА"     ', '  м. Київ, Шевченківський р-он, ', '   Проспект Перемоги, буд. 32   '"""
    for i in line:
        if len(i) <= 32:
            print(i)
        else:
            print(i.split())


with open('data.csv', 'r') as file:
    all_data = csv.reader(file, delimiter=';')
    for row in all_data:
        ZN = row.pop(0)
        FN = row.pop(0)
        row_transformer(row)

