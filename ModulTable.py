# coding: windows-1251
markers = {'РЕЦЕПЦІЯ', 'КAФЕ', 'ПТ', 'KFC', 'ТРЦ', 'ІД', 'ФОП', 'ТОВ', 'ПУНКТ', 'ПНФП', 'ОФІС', 'СКЛАД', 'ШВЕЙНА',
           'АВТОМИЙКА', 'ГЛОБУС', 'АРКАДІЯ', 'ПАРКУВАННЯ', 'ЮРИДИЧНА АДРЕСА', 'КРАМНИЦЯ', 'ЄДРПОУ', 'ЕДРПОУ', 'МАГАЗИН',
           'МАГ-Н', 'ВІДДІЛЕННЯ', 'ВИЇЗНА', 'САЛОН', 'КОМПЛЕКС', 'ЦЕНТР', 'КЛІНІКА', 'КАСА', 'ЄДРПОУ', 'СУПЕРМАРКЕТ',
           'ГІПЕРМАРКЕТ', 'СКЛАД-ТЕРМІНАЛ', 'АВТОСАЛОН', 'ЧЕРРІ', 'ЗАКУСОЧНА', 'СЕРВІСНИЙ', 'УКРПОШТА', 'РЕСТОРАН'}


def size(factory_number: str) -> int:
    """returns the maximum number of characters in the check cap"""
    model_rro = factory_number[2:4] if (factory_number[:2] == '40' or factory_number[:2] == '80') else factory_number[
                                                                                                       4:6]
    if model_rro == "23":
        return 36
    elif model_rro in ["22", "10", "21"]:
        return 42
    elif model_rro in ["01", "06", "11", "12", "13", "16", "17"]:
        return 32
    else:
        return 40


def check_markers(check: str) -> bool:
    return bool(markers.intersection(set(check.upper().split())))


def str_2_list(line_from_file: str) -> list:
    """convert and split line from file"""
    replaced_line = line_from_file.replace('"""', '"').replace('""', '"').replace('«', '"').replace('»', '"') \
        .replace('’', '\'').replace('\n', '').replace(',', ',roz').replace(';;', 'roz').replace(';;', 'roz') \
        .replace(';"', 'roz').replace(' ";', 'roz').replace(';', 'roz')
    return replaced_line.split('roz')


def cap2file(cap: list, file) -> None:
    pass


def line_creator():
    pass


if __name__ == "__main__":
    print(check_markers('пункт видачі'))
