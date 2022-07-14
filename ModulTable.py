markers = [
           "РЕЦЕПЦІЯ","Кафе","ПТ","KFC","ТРЦ","ІД","ФОП","ТОВ","ПУНКТ","ПНФП",
           "офіс","склад","Швейна","автомийка","Глобус","Аркадія","Паркування",
           "Юридична адреса","Крамниця","ЄДРПОУ","ЕДРПОУ","Магазин","Маг-н",
           "відділення","виїзна","салон","комплекс","центр","КЛІНІКА", "Каса",
           "ЄДРПОУ","Супермаркет","гіпермаркет","Склад-термінал","Автосалон",
           "Черрі", "Закусочна","сервісний","Укрпошта","Ресторан"
          ]


def size(str):
#"""returns the maximum number of characters in the check header"""
    if str[:2] == '40' or str[:2] == '80':
        str = str[2:4]
    else:
        str = str[4:6]
    if str == "23":
        return 36
    elif str == "24" or str == "20" :
        return 40
    elif str == "22" or str == "10" or str == "21":
        return 42
    elif str == str == "01" or str == "06" or str == "11" or str == "12" or \
         str == "13" or str == "16" or str == "17":
         return 32
    else: 
        return 40


def checkMarkers(check):
    for i in markers:
        if check.upper().find(i.upper()) >= 0:
            return True
    return False