# coding: windows-1251
import argparse
import ModulTable as Cap


def create_script(pos, mode=None, count: int = 0, ip=False):
    line = pos.pop(0).replace(" ", "").replace("AT", "АТ").replace("CП", "СП")
    length: int = Cap.size(line)
    writeTable.write('%Oper($$Data,"' + line + '",10,$$Flag)\n')  # generate string for the writing ZN
    writeTable.write('%If ($$Flag == 1)\n%Then\n')
    writeTable.write('%Set $$FN = "' + pos.pop(0).replace('?', '') + '"\n')  # generate string for the writing FN
    if mode == 'fop':
        # generate string for the writing ID
        writeTable.write('%Set $$ID = "' + pos.pop(0).replace('?', '').rjust(12) + '"\n')
    elif mode == 'tov':
        # generate string for the writing INN
        writeTable.write('%Set $$INN = "' + pos.pop(0).replace('?', '') + '"\n')
    if ip:
        # generate string for the writing IP
        writeTable.write('%Set $$IP = "' + pos.pop(0).replace('?', '') + '"\n')
        # generate string for the writing Gate
        writeTable.write('%Set $$Gate = "' + pos.pop(0).replace('?', '') + '"\n')
    line = None
    while pos:  # It's main loop for creating the recipt cap
        if Cap.check_markers(pos[0]):
            if line == None:
                line = pos.pop(0).lstrip().center(length)  #
            else:
                line = line.center(length)
        else:  # this or previous string don't have the markers
            if line == None:
                line = pos.pop(0).lstrip()
            elif len(line) + len(pos[0]) < length:
                line += ' ' + pos.pop(0).lstrip()
            elif len(line) + len(pos[0]) >= length:
                line = line.center(length)
        if len(pos) == 0:
            print("last line")
            line = line.center(length)
        print(str(len(line)) + ' VS ' + str(length))
        print(str(len(line)) + ':' + line)
        if len(line) == length:  # writing the header in to the file
            writeTable.write('22000000;' + str(count) + ';' + line.rstrip() + ';0;\n')
            print("write table")
            count += 1
            line = None


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', '--mode', type=str, help='mode  "metro", "tov" or "fop"')
    parser.add_argument('-i', '--ip', action='store_true', help='Add IP & getaway')
    parser.add_argument('-c', '--count', type=int, help='number of begin header')
    args = parser.parse_args()
    with open(r"data.csv", "r") as readTable:
        with open(r"OutData.txt", "w") as writeTable:
            for data in readTable:
                print("data in file")
                create_script(Cap.str_2_list(data))
                writeTable.write('%Else\n%EndIf\n\n')

