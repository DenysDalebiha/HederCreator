markers = [
    "РЕЦЕПЦІЯ", "Кафе", "ПТ", "KFC", "ТРЦ", "ІД", "ФОП", "ТОВ", "ПУНКТ", "ПНФП",
    "офіс", "склад", "Швейна", "автомийка", "Глобус", "Аркадія", "Паркування",
    "Юридична адреса", "Крамниця", "ЄДРПОУ", "ЕДРПОУ", "Магазин", "Маг-н",
    "відділення", "виїзна", "салон", "комплекс", "центр", "КЛІНІКА", "Каса",
    "ЄДРПОУ", "Супермаркет", "гіпермаркет", "Склад-термінал", "Автосалон",
    "Черрі", "Закусочна", "сервісний", "Укрпошта", "Ресторан"
]


def size(factory_number: str) -> int:
    """returns the maximum number of characters in the check header"""
    model_rro = factory_number[2:4] if (factory_number[:2] == '40' or factory_number[:2] == '80') else factory_number[4:6]
    if model_rro == "23":
        return 36
    elif model_rro in ["24", "20"]:
        return 40
    elif model_rro in ["22", "10", "21"]:
        return 42
    elif model_rro in ["01", "06", "11", "12", "13", "16", "17"]:
        return 32
    else:
        return 40


def check_markers(check):
    for i in markers:
        if check.upper().find(i.upper()) >= 0:
            return True
    return False


def str_2_list(line_from_file: str) -> list:
    """convert and split line from file"""
    replaced_line = line_from_file.replace('"""', '"').replace('""', '"').replace('«', '"').replace('»', '"') \
        .replace('’', '\'').replace('\n', '').replace(',', ',roz').replace(';;', 'roz').replace(';;', 'roz') \
        .replace(';"', 'roz').replace(' ";', 'roz').replace(';', 'roz')
    return replaced_line.split('roz')


if __name__ == "__main__":
    print(size("402305678"))
