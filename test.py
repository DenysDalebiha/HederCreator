# coding: windows-1251
import csv
import ModulTable as Cap


def row_transformer(line: list) -> list:
    """ line = ['�ȯ������ �����ò���� ���� ������������������ ��������', '"�I����� ����"',
    '�. ���, ������������� �-��, �������� ��������, ���. 32']
    return ['   �ȯ������ �����ò���� ����   ', '   ������������������ ��������   ',
      '      "�I����� ����"     ', '  �. ���, ������������� �-��, ', '   �������� ��������, ���. 32   '"""
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

