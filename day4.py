# integer - tip dannyh , predstavlyaent celie chisla ot -beskonechnosti do + 
# float - drobnie chisla
# boolean True False 
# string - ""

# text = 'hello world'

# print(text[:6])  - first word till index 5 added
# print(text[4:]) - end of word from index 4 added
# prnt(text[4:6])

# start = 7
# step = 2
# stop = 4

# print(text(start:stop:step))



# text = "12345654"
# start = 3
# stop = 9
# step = 3
# print(text[2:6:1])
# print(text[::4])


# word =  input("Enter word: ")
# reversed_word = word[::-1]
# print(reversed_word == word)

# Тернарные операторы = if elif else 
# Тернарный оператор в Python - это способ записи условия в одну строку. 
# Он позволяет назначить значение переменной в зависимости от выполнения условия. Формат тернарного оператора выглядит следующим образом:
# x = значение_если_условие_истинно if условие else значение_если_условие_ложно
# Это похоже на стандартное условие if-else, но с более компактным синтаксисом. Если условие истинно, переменной x будет назначено 
# значение значение_если_условие_истинно, в противном случае оно будет назначено значение_если_условие_ложно.

# word =  input("Enter word: ")
# reversed_word = word[::-1]
# result = "Polindrom" if word == reversed_word else 'Ne polindrom'
# print(result)

# dividetoupandlow = input("Enter text: ")
# count = len(dividetoupandlow)
# halfpart = round(count / 2)
# firstp = dividetoupandlow[:halfpart].upper()
# secondp = dividetoupandlow[halfpart:].lower()
# print(firstp + secondp)

# 1. Напишите программу, которая проверяет, является ли введенное пользователем число четным или нечетным, и выводит соответствующее сообщение.
# text = float(input("Enter num: "))
# x = text % 2
# if x == 0:
#     print("Num is even")
# else:
#     print("Num is odd")


# 2. Создайте программу, которая запрашивает у пользователя его возраст и выводит сообщение о том, можно ли ему получить права водителя 
# в соответствии с законом (если возраст больше или равен 18).
# age = float(input("Enter age: "))
# if age >= 18:
#     print("U can get the rights")
# else:
#     print("U r too young to get rights")
# 3. Напишите программу, которая проверяет, является ли введенное пользователем число положительным, отрицательным или нулем, и выводит соответствующее
# сообщение.
# num = float(input("Enter num: "))
# if num > 0:
#     print("num is pos")
# elif num < 0:
#     print('num is negative')
# else:
#     print("Num is zero")

# 4. Разработайте программу, которая запрашивает у пользователя его оценку (от 0 до 100) и выводит сообщение о его успехах в зависимости от полученной 
#оценки (например, "Отлично", "Хорошо", "Удовлетворительно", "Неудовлетворительно").


# mark = int(input("Enter mark 0-100: "))
# if 0 <= mark < 25:
#     print("Neudov")
# elif  25 <= mark < 50:
#     print("Udov")
# elif 50 <= mark < 75:
#     print("Good")
# elif 75 <= mark <= 100:
#     print("Excellent")
# else:
#     ("Error")



# 5. Создайте программу, которая запрашивает у пользователя его имя и проверяет, начинается ли его имя с буквы "А" (или любой другой заданной буквы), 
# и выводит соответствующее сообщение.


# name = input("Enter name: ")
# if name.startswith(("a", "A", "а", "А")):
#     print("Starts with A")
# else:
#     print("Incorrect, start name from A")


# # 6. Напишите программу, которая запрашивает у пользователя пароль и проверяет, соответствует ли он заданным требованиям
# безопасности (например, содержит ли пароль хотя бы одну цифру, одну букву в верхнем регистре и один специальный символ).

# import re

# def check_password_strength(password):
#     # Проверка наличия хотя бы одной цифры
#     if not re.search(r'\d', password):
#         return False

#     # Проверка наличия хотя бы одной буквы в верхнем регистре
#     if not re.search(r'[A-Z]', password):
#         return False

#     # Проверка наличия хотя бы одного специального символа
#     if not re.search(r'[!@#$%^&*()\-_=+{};:,<.>]', password):
#         return False

#     # Если все требования выполнены, возвращаем True
#     return True

# def main():
#     password = input("Введите пароль: ")

#     if check_password_strength(password):
#         print("Пароль удовлетворяет требованиям безопасности.")
#     else:
#         print("Пароль не удовлетворяет требованиям безопасности.")


# main()


# 7. Разработайте программу, которая запрашивает у пользователя два числа и выводит наибольшее из них.
# number1 = int(input("Enter 1st num: "))
# number2 = int(input("Enter 2nd num: "))
# if number1 > number2:
#     print(number1)
# else:
#     print(number2)


# 8. Создайте программу, которая проверяет, является ли введенная пользователем строка палиндромом (т.е. одинаково читается слева направо и справа налево).
# text = input("Enter Polindrom:")
# if text == text[::-1]:
#     print("Polindrom")
# else:
#     print("Nepoly")

# 9. Напишите программу, которая определяет тип треугольника по введенным пользователем длинам его сторон (равносторонний, равнобедренный или разносторонний).
# a = int(input("Enter a: "))
# b = int(input("Enter b: "))
# c = int(input("Enter c: "))

# if a == b and b == c:
#     print("Triangle with equal sides")
# elif a == b or b == c or a == c:
#     print("Two sides equal triangle")
# else:
#     print("Triangle with different sides")

# 10. Разработайте программу, которая запрашивает у пользователя текущий месяц и день и выводит сообщение о сезоне года, соответствующем этой дате.
# def get_season(month, day):
#     # Создаем словарь, в котором ключами являются названия сезонов, а значениями - списки месяцев, входящих в каждый сезон
#     seasons = {
#         'зима': [(12, 1), (1, 2), (2, 3)],
#         'весна': [(3, 1), (4, 2), (5, 3)],
#         'лето': [(6, 1), (7, 2), (8, 3)],
#         'осень': [(9, 1), (10, 2), (11, 3)]
#     }

#     # Преобразуем введенные пользователем данные в числа
#     month = int(month)
#     day = int(day)

#     # Проверяем каждый сезон
#     for season, months in seasons.items():
#         for start_month, duration in months:
#             end_month = (start_month + duration - 1) % 12 + 1
#             # Проверяем, входит ли введенная пользователем дата в текущий сезон
#             if (month == start_month and day >= 1) or (month == end_month and day <= 31) or (start_month < month < end_month):
#                 return season

#     return "Некорректная дата"

# def main():
#     month = input("Введите текущий месяц (число от 1 до 12): ")
#     day = input("Введите текущий день (число от 1 до 31): ")

#     season = get_season(month, day)
#     print("Сезон года, соответствующий введенной дате:", season)

# main()


