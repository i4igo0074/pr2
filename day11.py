# import main
# print(main.streents)

# from main import streents as st
# print(st)

# from string import ascii_letters as a
# print(a)


# import os
# os.system("ls")
# os.system("clear")

# path = os.getcwd() + "/main.py" #shows where main.py located
# print(path)

# os.mkdir("new_folder")
# os.rmdir("new_folder")

# import sys

# if sys.argv[1] == "runbot":
#     print("Bot active")
# elif sys.argv[1] == "runserver":
#     print("server active")

# print(sys.platform)

# from main import streents
# from random import randint, randrange, choice, shuffle
# print(randint(1,9), randrange(1,100,5))

# import random as rd
# print(rd.randint(1,9)), randrange(0,100,5), choice("dsfdsf")
# street = choice(streents)
# number = randint(1,500)
# address = f"Улица {street} {number}"
# print(address)

# print(shuffle(streents))   #shuffle mixes evrthng
# print(streents)


# from main import streents
# from random import randint, randrange, choice, shuffle
# list1 = []
# for i in range(1,6):
# list1 = [1,2,3,4,5,6]
# shuffle(list1)
# print(list1[0], list1[2])

# ball = {
#     "two similar": 2,
#     "sum >= 10": 3,
#     "if one of them 6": 1
# }
# list1 = [1,2,3,4,5,6]
# points_list = []

# for i in range(1,6):
#     shuffle(list1)
#     suml = list1[0] + list1[1]
#     print(f"Кость 1 = {list1[0]}, Кость = {list1[1]}")
#     if suml >= 10:
#         points_list.append(3)
#         print(f"Congrats {suml} >= 10")
#     elif list1[0] == list1[1]:
#         points_list.append(2)
#         print("Added 2 points")
#     elif list1[0] == 6 or list1[1] == 6:
#         points_list.append(1)
#         print("Added 1 point")
# sump = sum(points_list)
# if sump >= 10:
#     print("U win the game")
# else:
#     print("U lose")
# print(list1[0], list1[2])

    

# while True:
#     options = ["st","sc","pa"]
#     ch1= choice(options)
#     ch2 = input("Enter choice: ")
#     print(ch1, ch2)
#     if ch1 == ch2:
#         print("noone won")
#     elif ch1 == 'st' and ch2 == "sc":
#         print("comp won")
#     elif ch1 == 'st' and ch2 == "pa":
#         print("human won")
#     elif ch1 == "sc" and ch2 == 'st':
#         print("human won")
#     elif ch1 == "sc" and ch2 == 'pa':
#         print("comp won")
#     elif ch1 == "pa" and ch2 == 'sc':
#         print("human won")
#     elif ch1 == "pa" and ch2 == 'st':
#         print("comp won")


# Игра "Угадай число":
# Напишите программу, в которой компьютер загадывает случайное число, а игрок должен угадать его. 
# Программа должна давать подсказки ("слишком большое" или 
# "слишком маленькое") и вести подсчет попыток.

# attemts = 0
# while True:
#     comp = randint(1,9)
#     print("Comps num:", comp) #for knowing value of comp
#     if 1 <= comp <= 4:
#         print("Clue - Lower")
#     elif 5 <= comp <= 9:
#         print("Clue - Higher")
#     for i in range(3):
#         hn = int(input("Enter num 1-9: "))
#         if comp == hn:
#             attemts += 1
#             print("U guessed")
#             print(attemts)
#         else:
#             attemts += 1
#             print("u failed")
#             print(attemts)






# Генератор паролей:
# Создайте программу, которая генерирует случайный пароль заданной длины для пользователя. Пароль должен содержать буквы верхнего и нижнего регистров, цифры 
# и специальные символы.
# import random
# while True:

#     num = input('login ')
#     pas = ''
#     for x in range(8): #Количество символов (8)
#         pas = pas + random.choice(list('1234567890abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ!@#$%^&*()-=_+[]{};:,.<>?/')) #Символы, из которых будет составлен пароль
#     print('Hello, ', num, 'your password is: ', pas)




# Случайное перемешивание слов в предложении:
# Напишите программу, которая принимает предложение от пользователя и случайным образом перемешивает слова в этом предложении, сохраняя первую и последнюю 
# буквы каждого слова на месте.

# не знаю как сделать
# Имитация игрового казино:
# Создайте простую имитацию игры в казино, например, рулетку или игровые автоматы. Используйте модуль random для генерации случайных результатов 
# и взаимодействия с пользователем.
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



# Генератор случайных дат:
# Напишите программу, которая генерирует случайную дату в определенном временном диапазоне (например, за последние 10 лет). Используйте модуль
# random для генерации чисел и создания даты.

# from random import randint


# dd = randint(1,31)
# mm = randint(1,12)
# yy = randint(2014,2024)
# print(f"{dd}.{mm}.{yy}")