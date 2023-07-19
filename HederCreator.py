# coding: windows-1251
import argparse
import csv
import ModulTable as Header

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', '--mode', type=str, help='mode  "metro", "tov" or "fop"')
    parser.add_argument('-i', '--ip', action='store_true', help='Add IP & getaway')
    parser.add_argument('-c', '--count', type=int, help='number of begin header')
    args = parser.parse_args()
    with open('data.csv', 'r') as input_file:
        with open('OutData.txt', 'w') as output_file:
            all_data = csv.reader(input_file, delimiter=';')
            for row in all_data:
                Header.create_script(row, output_file, args.mode, args.ip, args.count)

