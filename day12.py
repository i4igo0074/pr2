# from time import sleep

# from random import randint, randrange, choice, shuffle


# options = ["ap","pi","le", "gr", "ma"]
# count = 0

# for i in range(1, 200):
#     ch1 = choice(options)
#     ch2 = choice(options)
#     ch3 = choice(options)
#     ch4 = choice(options)
#     ch5 = choice(options)

#     print(ch1, ch2, ch3, ch4, ch5)
#     count += 1
#     print(count)
#     if ch1 == ch2 == ch3==ch4==ch5:
#         print("U won")
#         break
# else:
#     print("U lost")
#     sleep(0.2)


# import time
# print(time.sleep(2))

# print(time.time()) # секунд прошло с 1970 года

# print(time.localtime()) # дата и время
# print(time.asctime()) # дата и время


# import datetime

# now = datetime.datetime.now()
# print(now.strftime("%d-%m-%Y %H:%M:%S"))

# today = datetime.date.today()
# print(today + datetime.timedelta(days=5))

# my_birthday = datetime.date(2000, 6, 26)
# print((today - my_birthday) * 24 * 60 * 60)



# from math import pi, e, sin, cos, tan, log, sqrt
# print(sqrt(2500))

# import json

# data = {'name': 'John', 'age': 25, 'city': 'New York'}

# Кодирование данных в JSON
# json_str = json.dumps(data)
# print(json_str)

# Запись в файл JSON и кодирование данных в JSON
# with open('data.json', 'w') as file:
#     json.dump(data, file)

# Чтение из файла JSON и декодирование данных в Python
# with open('data.json', 'r') as file:
#     # Декодирование JSON из файла
#     data = json.load(file)

# print(data)

# from random import randint, randrange, choice, shuffle

# streets = ["Abay", "Seyfullina","Manas","Abilay"]
# nums = list(range(1,101))

# asd = set()
# while len(asd) != 100:
#     a = choice(streets)
#     b = choice(nums)
#     asd.add(f"st {a} {b}")

# print(asd)

# from random import randint, randrange, choice, shuffle
# names = ["Иван", "Петр", "Алексей", "Михаил", "Андрей", "Сергей", "Дмитрий", "Николай", "Владимир", "Константин", "Егор", "Игорь", "Станислав", "Федор", "Борис"]
# surnames = ["Иванов", "Петров", "Сидоров", "Смирнов", "Кузнецов", "Васильев", "Попов", "Соколов", "Михайлов", "Новиков", "Федоров", "Морозов", "Волков", "Алексеев", "Лебедев"]

# list_unique = set()
# while len(list_unique) != 101:
#     a = choice(names)
#     b = choice(surnames)
#     list_unique.add(f"{a} {b}")
# print(list_unique)

# from random import randint, randrange, choice, shuffle

# # listn = set()
# # nums = list(range(12345,100000))

# # while len(listn) != 101:
# #     n = choice(nums)
# #     listn.add(f"+7{n}")
# # print(listn)

# # +7 707 9450011
# a = set()
# while len(a) != 100:
    
#     numb = f"+7 {choice([707,708,777,705,747])} {randint(1000000, 9999999)}"
#     a.add(numb)
# print(a)
    
# У вас уже есть 100 адресов
# 100 номеров телефонов
# 100 Фио

# Задачи:
# 1. Сгенерировать 100 email

# from random import randrange, randint, choice, shuffle

# lemail = set()
# while len(lemail) != 100:
#     a = ''.join(choice('abcdefghijklmnopqrstuvwxyz') for _ in range(5))
#     b = randint(0,100)
#     c = choice(["bk.ru", "mail.ru", "list.ru", "input.ru"])
#     lemail.add(f"{a}{b}@{c}")
# print(lemail)


# 2. Сгенерировать 100 паролей
# from random import randrange, randint, choice, shuffle

# lkeys = set()
# while len(lkeys) != 100:
#     a = ''.join(choice('1234567890abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ!@#$%^&*()-=_+[]{};:,.<>?/') for _ in range(8))
#     lkeys.add(a)
# print(lkeys)



# 3. Сгенерировать 100 адресов = 'г. Москва, ул. Алиева, д. 1, кв. 1'
# streets = [
#     "Main Street",
#     "Elm Street",
#     "Oak Avenue",
#     "Pine Road",
#     "Maple Drive",
#     "Cedar Lane",
#     "Birch Street",
#     "Willow Avenue",
#     "Juniper Lane",
#     "Sycamore Avenue"
# ]

# from random import randrange, randint, choice, shuffle

# lad = set()
# while len(lad) != 100:
#     lad.add(f"г.Москва, ул.{choice(streets)}, д.{randint(1,30)}, кв.{randint(1,80)}")
# print(lad)

# 4. Сгенерировать 100 дат рождения = '1990-01-01'
from random import randrange, randint, choice, shuffle

# ldat = set()
# while len(ldat) != 100:
#     ldat.add(f"{randint(1970,2005)}-{randint(1,12)}-{randint(1,30)}")


# users = {"date_of_birth", ""}
# users.add(ldat)
# print(users)


# from random import randint, randrange, choice, shuffle

# import json
# users = [
# {
# 'id': 1,
# 'full': 'Иванов Иван Иванович',
# 'phone': '000000000000',
# 'email': 'example@example.com',
# 'password': 'XXXXXXXX',
# 'address': 'г. Москва, ул. Алиева, д. 1, кв. 1',
# 'date_of_birth': '1990-01-01',
# },
# {
# 'id': 2,
# 'full': 'Иванов Иван Иванович',
# 'phone': '000000000000',
# 'email': 'example@example.com',
# 'password': 'XXXXXXXX',
# 'address': 'г. Москва, ул. Алиева, д. 1, кв. 1',
# 'date_of_birth': '1990-01-01',
# },
# {
# 'id': 3,
# 'full': 'Иванов Иван Иванович',
# 'phone': '000000000000',
# 'email': 'example@example.com',
# 'password': 'XXXXXXXX',
# 'address': 'г. Москва, ул. Алиева, д. 1, кв. 1',
# 'date_of_birth': '1990-01-01',
# }
# ]





# names = ["Иван", "Петр", "Алексей", "Михаил", "Андрей", "Сергей", "Дмитрий", "Николай", "Владимир", "Константин", "Егор", "Игорь", "Станислав", "Федор", "Борис"]
# surnames = ["Иванов", "Петров", "Сидоров", "Смирнов", "Кузнецов", "Васильев", "Попов", "Соколов", "Михайлов", "Новиков", "Федоров", "Морозов", "Волков", "Алексеев", "Лебедев"]

# list_unique = set()
# while len(list_unique) != 101:
#     a = choice(names)
#     b = choice(surnames)
#     list_unique.add(f"{a} {b}")
#     for i in list_unique:
        






# import json
# users = [
# {
# 'id': 1,
# 'full': 'Иванов Иван Иванович',
# 'phone': '000000000000',
# 'email': 'example@example.com',
# 'password': 'XXXXXXXX',
# 'address': 'г. Москва, ул. Алиева, д. 1, кв. 1',
# 'date_of_birth': '1990-01-01',
# },
# {
# 'id': 2,
# 'full': 'Иванов Иван Иванович',
# 'phone': '000000000000',
# 'email': 'example@example.com',
# 'password': 'XXXXXXXX',
# 'address': 'г. Москва, ул. Алиева, д. 1, кв. 1',
# 'date_of_birth': '1990-01-01',
# },
# {
# 'id': 3,
# 'full': 'Иванов Иван Иванович',
# 'phone': '000000000000',
# 'email': 'example@example.com',
# 'password': 'XXXXXXXX',
# 'address': 'г. Москва, ул. Алиева, д. 1, кв. 1',
# 'date_of_birth': '1990-01-01',
# }
# ]




# print(data)

# from random import randint, randrange, choice, shuffle

# streets = ["Abay", "Seyfullina","Manas","Abilay"]
# nums = list(range(1,101))

# asd = set()
# while len(asd) != 100:
#     a = choice(streets)
#     b = choice(nums)
#     asd.add(f"st {a} {b}")

# print(asd)

# from random import randint, randrange, choice, shuffle
# names = ["Иван", "Петр", "Алексей", "Михаил", "Андрей", "Сергей", "Дмитрий", "Николай", "Владимир", "Константин", "Егор", "Игорь", "Станислав", "Федор", "Борис"]
# surnames = ["Иванов", "Петров", "Сидоров", "Смирнов", "Кузнецов", "Васильев", "Попов", "Соколов", "Михайлов", "Новиков", "Федоров", "Морозов", "Волков", "Алексеев", "Лебедев"]

# list_unique = set()
# while len(list_unique) != 101:
#     a = choice(names)
#     b = choice(surnames)
#     list_unique.add(f"{a} {b}")
# print(list_unique)

# from random import randint, randrange, choice, shuffle

# # listn = set()
# # nums = list(range(12345,100000))

# # while len(listn) != 101:
# #     n = choice(nums)
# #     listn.add(f"+7{n}")
# # print(listn)

# # +7 707 9450011
# a = set()
# while len(a) != 100:
    
#     numb = f"+7 {choice([707,708,777,705,747])} {randint(1000000, 9999999)}"
#     a.add(numb)
# print(a)
    
# У вас уже есть 100 адресов
# 100 номеров телефонов
# 100 Фио

# Задачи:
# 1. Сгенерировать 100 email

# from random import randrange, randint, choice, shuffle

# lemail = set()
# while len(lemail) != 100:
#     a = ''.join(choice('abcdefghijklmnopqrstuvwxyz') for _ in range(5))
#     b = randint(0,100)
#     c = choice(["bk.ru", "mail.ru", "list.ru", "input.ru"])
#     lemail.add(f"{a}{b}@{c}")
# print(lemail)


# 2. Сгенерировать 100 паролей
# from random import randrange, randint, choice, shuffle

# lkeys = set()
# while len(lkeys) != 100:
#     a = ''.join(choice('1234567890abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ!@#$%^&*()-=_+[]{};:,.<>?/') for _ in range(8))
#     lkeys.add(a)
# print(lkeys)



# 3. Сгенерировать 100 адресов = 'г. Москва, ул. Алиева, д. 1, кв. 1'
# streets = [
#     "Main Street",
#     "Elm Street",
#     "Oak Avenue",
#     "Pine Road",
#     "Maple Drive",
#     "Cedar Lane",
#     "Birch Street",
#     "Willow Avenue",
#     "Juniper Lane",
#     "Sycamore Avenue"
# ]

# from random import randrange, randint, choice, shuffle

# lad = set()
# while len(lad) != 100:
#     lad.add(f"г.Москва, ул.{choice(streets)}, д.{randint(1,30)}, кв.{randint(1,80)}")
# print(lad)

# 4. Сгенерировать 100 дат рождения = '1990-01-01'
from random import randrange, randint, choice, shuffle

# ldat = set()
# while len(ldat) != 100:
#     ldat.add(f"{randint(1970,2005)}-{randint(1,12)}-{randint(1,30)}")


# users = {"date_of_birth", ""}
# users.add(ldat)
# print(users)


from random import randint, randrange, choice, shuffle

import json


def fname():
    from random import randint, randrange, choice, shuffle
    names = ["Иван", "Петр", "Алексей", "Михаил", "Андрей", "Сергей", "Дмитрий", "Николай", "Владимир", "Константин", "Егор", "Игорь", "Станислав", "Федор", "Борис"]
    surnames = ["Иванов", "Петров", "Сидоров", "Смирнов", "Кузнецов", "Васильев", "Попов", "Соколов", "Михайлов", "Новиков", "Федоров", "Морозов", "Волков", "Алексеев", "Лебедев"]

    list_unique = set()
    while len(list_unique) != 101:
        a = choice(names)
        b = choice(surnames)
        list_unique.add(f"{a} {b}")
    return list_unique


def nums():
    
    a = set()
    while len(a) != 100:
        numb = f"+7 {choice([707,708,777,705,747])} {randint(1000000, 9999999)}"
        a.add(numb)
    return a


def mails():
    lemail = set()
    while len(lemail) != 100:
        a = ''.join(choice('abcdefghijklmnopqrstuvwxyz') for _ in range(5))
        b = randint(0,100)
        c = choice(["bk.ru", "mail.ru", "list.ru", "input.ru"])
        lemail.add(f"{a}{b}@{c}")
    return lemail

def key():
    lkeys = set()
    while len(lkeys) != 100:
        a = ''.join(choice('1234567890abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ!@#$%^&*()-=_+[]{};:,.<>?/') for _ in range(8))
        lkeys.add(a)
    return lkeys
print(key())


def adress():
    streets = [
    "Main Street",
    "Elm Street",
    "Oak Avenue",
    "Pine Road",
    "Maple Drive",
    "Cedar Lane",
    "Birch Street",
    "Willow Avenue",
    "Juniper Lane",
    "Sycamore Avenue"
]
    lad = set()
    while len(lad) != 100:
        lad.add(f"г.Москва, ул.{choice(streets)}, д.{randint(1,30)}, кв.{randint(1,80)}")
    return lad

def bdate():
    ldat = set()
    while len(ldat) != 100:
        ldat.add(f"{randint(1970,2005)}-{randint(1,12)}-{randint(1,30)}")
    return ldat



users = []
names_list = list(fname())
num_list = list(nums())
mail_list = list(mails())
key_list = list(key())
adress_list = list(adress())
bdate_list = list(bdate())

for i in range(1,101):
    
    full_name = choice(names_list)
    names_list.remove(full_name)
    
    full_num = choice(num_list)
    num_list.remove(full_num)

    full_male = choice(mail_list)
    mail_list.remove(full_male)

    full_key = choice(key_list)
    key_list.remove(full_key)

    full_adress = choice(adress_list)
    adress_list.remove(full_adress)

    full_bdate = choice(bdate_list)
    bdate_list.remove(full_bdate)

    user = [
    {
    'id': i,
    'full': full_name,
    'phone': full_num,
    'email': full_male,
    'password': full_key,
    'address': full_adress,
    'date_of_birth': full_bdate,
    } ]
    users.append(user)
import json


with open('data.json', 'w', encoding='utf-8') as file:
    json.dump(users, file, ensure_ascii=False, indent=4)
