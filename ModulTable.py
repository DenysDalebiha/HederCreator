# coding: windows-1251
import logging
from datetime import datetime

logging.basicConfig(level=logging.INFO, filename='header.log', filemode='a')

markers = {'РЕЦЕПЦІЯ', 'КAФЕ', 'ПТ', 'KFC', 'ТРЦ', 'ІД', 'ФОП', 'ТОВ', 'ПУНКТ', 'ПНФП', 'ОФІС', 'СКЛАД', 'ШВЕЙНА',
           'БАР', 'АВТОМИЙКА', 'ГЛОБУС', 'АРКАДІЯ', 'ПАРКУВАННЯ', 'ЮРИДИЧНА', 'АДРЕСА', 'КРАМНИЦЯ', 'КЛІНІКА', 'КАСА',
           'ЄДРПОУ', 'ЕДРПОУ', 'МАГАЗИН', 'МАГ-Н', 'КАФЕТЕРІЙ', 'ВІДДІЛЕННЯ', 'ВИЇЗНА', 'САЛОН', 'КОМПЛЕКС', 
           'СУПЕРМАРКЕТ', 'ГІПЕРМАРКЕТ', 'СКЛАД-ТЕРМІНАЛ', 'АВТОСАЛОН', 'ЧЕРРІ', 'ЗАКУСОЧНА', 'СЕРВІСНИЙ', 'ЦЕНТР', 
           'УКРПОШТА', 'РЕСТОРАН', 'ПН411350026567', 'VIVAT', 'ЗАКЛАД', 'ТЕЛ.', 'WWW'}


def size(factory_number: str) -> int:
    """returns the maximum number of characters in the check cap"""
    model_rro = factory_number[2:4] if (factory_number[:2] == '40' or factory_number[:2] == '80') else factory_number[
                                                                                                       4:6]
    if model_rro == "23":
        char_limit = 36
    elif model_rro in ["22", "10", "21"]:
        char_limit = 42
    elif model_rro in ["01", "06", "11", "12", "13", "16", "17"]:
        char_limit = 32
    else:
        char_limit = 40
    logging.debug(f'char_limit = {char_limit}')
    return char_limit


def check_markers(check: str, size_of_header: int = 32) -> str:
    if markers.intersection(set(check.upper().replace('"', '').replace('-', ' ').replace('(', ' ').replace('.', ' ').split())):
        return check.center(size_of_header)
    else:
        return check


def str_spliter(line: str) -> list:
    """ return split line
    >>>str_spliter("КИЇВСЬКИЙ ЗООЛОГІЧНИЙ ПАРК ЗАГАЛЬНОДЕРЖАВНОГО ЗНАЧЕННЯ")
    ['КИЇВСЬКИЙ ', 'ЗООЛОГІЧНИЙ ', 'ПАРК ', 'ЗАГАЛЬНОДЕРЖАВНОГО ', 'ЗНАЧЕННЯ']
    >>>str_spliter('м. Київ, Шевченківський р-он, Проспект Перемоги, буд. 32')
    ['м. Київ,', ' Шевченківський р-он,', ' Проспект Перемоги,', ' буд. 32']
    """
    split_str = line.replace(', ', ',^ ').split('^')
    if len(split_str) == 1:
        split_str = line.replace(',', ' ^').split('^')
        if len(split_str) == 1:
            split_str = line.replace(' ', ' ^').split('^')
            if len(split_str) == 1:
                logging.critical(f'{datetime.now().isoformat()} unsplittable string')
                return split_str
    logging.debug(f'{datetime.now().isoformat()}line {line} split to \n{split_str}')
    return split_str


def str_replace(str_: str) -> str:
    return str_.replace('«', '"').replace('»', '"').replace('’', '\'').replace('\n', '')


def header_line(line, limit=32, left=False) -> str:
    """return one element of header"""
    out = ''
    while len(out) < limit:
        line[0] = str_replace(check_markers(line[0]))
        if len(line[0]) > limit:
            line[0:0] = str_spliter(line.pop(0).lstrip())
        if line and (len(out) + len(line[0]) <= limit):
            out += check_markers(line.pop(0), limit)
        if len(line) == 0:
            return out.strip() if left else out.center(limit).rstrip()
        if len(line[0]) > limit:
            line[0:0] = str_spliter(line.pop(0).lstrip())
        line[0] = check_markers(line[0], limit)
        if len(out) == limit:
            return out.strip() if left else out.center(limit).rstrip()
        elif line and (len(out) + len(line[0]) <= limit):
            out += str_replace(line.pop(0))
        else:
            return out.strip() if left else out.center(limit).rstrip()
        if len(line) == 0:
            return out.strip() if left else out.center(limit).rstrip()
    return out.strip() if left else out.center(limit).rstrip()

def create_script(line, file, mode, ip=False, offset: int = 0):
    while len(line[-1]) == 0:
        line.pop(-1)
    header = []
    factory_number = line.pop(0).replace(" ", "").replace("AT", "АТ").replace("CП", "СП")
    fiscal_number = line.pop(0)
    limit = size(factory_number)
    if ip:
        ip_address = line.pop(0)
        gate = line.pop(0)
    else:
        ip_address, gate = None, None
    idd = line.pop(0) if mode == 'fop' else None
    while line:
        if mode == 'metro':
            header.append(header_line(line, limit, left=True))
        else:
            header.append(header_line(line, limit))
    count = int(offset) if offset else 0
    header_to_file(file, factory_number, fiscal_number, header, ip_address, gate,
                   idd, mode, count)
    logging.info(f'{datetime.now().isoformat()}, {factory_number}, {fiscal_number}, {header}, {ip_address}, {gate}, '
                 f'{idd}, {mode}, {count}')


def header_to_file(out_file, factory_number: str, fiscal_number: str, header: list, ip_address, gate,
                   idd, mode, offset) -> None:
    """write one cap to file"""
    out_file.write(f'%Oper($$Data,"{factory_number}",10,$$Flag)\n%If ($$Flag == 1)\n%Then\n')
    out_file.write(f'%Set $$FN = "{fiscal_number}"\n')
    if mode == 'fop':
        # generate string for the writing IDD
        out_file.write(f'%Set $$ID = "{idd.replace("?", "").rjust(12)}"\n')
    elif mode == 'tov':
        # generate string for the writing INN
        out_file.write(f'%Set $$INN = "{idd.replace("?", "")}"\n')
    if ip_address:
        # generate string for the writing IP
        out_file.write(f'%Set $$IP = "{ip_address.replace("?", "")}"\n')
        # generate string for the writing Gate
        out_file.write(f'%Set $$Gate = "{gate.replace("?", "")}"\n')
    for index, item in enumerate(header):
        out_file.write(f'22000000;{index + offset};{item};0;\n')
    out_file.write('%Else\n%EndIf\n\n')
