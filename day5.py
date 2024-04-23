# list - []
# tuple - ()

# list1 = []
# list.append(1) add in End of code
# list.insert(2,9) add index add num or text to list
# list.extend() sort through list

# months = ['January', 'March', 'April', 'May', 'June', 
#           'July', 'August', 'September', 'October', 'November', 'December']
# months.insert(1, 'February')
# print(months)

# months[5] = 'Июнь'

# print(months)




# months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
# months.sort() # сортирует по алфавиту
# months.sort(reverse=True) # сортирует по алфавиту в обратном порядке
# print(months)




# numbers = [0,3,4,2,1,5,7,6,8,9]
# numbers.sort() # разворачивает список
# print(numbers)




# list1 = [['hello', 12], ['ok',5], ['the', 23], ['bye', 6]]

# list1.sort(key=lambda x: x[0]) # сортирует по имени
# print(list1)

# list1.sort(key=lambda x: x[1], reverse=True) # сортирует количеству
# print(list1)




# list1 = [['hello', 12], ['ok',5], ['the', 23], ['bye', 6]]

# list1.sort(key=lambda x: x[0]) # сортирует по имени
# print(list1)

# list1.sort(key=lambda x: x[1], reverse=True) # сортирует количеству
# print(list1)




# name = ('Ali', 'Ali', 'Vali', 'Sali')
# print(type(name))

# print(name.index('Ali'))
# print(name.count('Ali'))

# list = []
# num1 = int(input("Enter num: "))
# list.append(num1)
# num2 = int(input("Enter num2: "))
# list.append(num2)
# num3 = int(input("Enter num3"))
# list.append(num3)
# num4 = int(input("Enter num4"))
# list.append(num4)
# num5 = int(input("Enter num5"))
# list.append(num5)
# print(list)


# list = []
# list.extend([int(input("Enter num: ")), int(input("Enter num2: "))])
# print(list)

# list1 = []
# nums = input("Enter nums: ").split()
# list1.extend(nums)
# list1 = list(map(int, list1))
# print(list1)

# min max sum     print(min(list1))


# № 1
# создайте 2 пустых листа
# list_1 = []
# list_2 = []
# спросите у пользователя 5 чисел
# если он четный добавте его в первый список
# иначе на другой
# в конце вывести оба списока



# list_1 = []
# list_2 = []

# num1 = int(input("Enter the first number: "))
# if num1 % 2:
#     list_1.append(num1)
# else:
#     list_2.append(num1)

# num2 = int(input("Enter the second number: "))
# if num2 % 2:
#     list_1.append(num2)
# else:
#     list_2.append(num2)

# num3 = int(input("Enter the third number: "))
# if num3 % 2:
#     list_1.append(num3)
# else:
#     list_2.append(num3)

# num4 = int(input("Enter the fourth number: "))
# if num4 % 2:
#     list_1.append(num4)
# else:
#     list_2.append(num4)

# num5 = int(input("Enter the fifth number: "))
# if num5 % 2:
#     list_1.append(num5)
# else:
#     list_2.append(num5)

# print("List 1:", list_1)
# print("List 2:", list_2)







# № 2
# создайте 1 лист
# спросите у пользователя 5 чисел и добавте его в список 
# и определите самое большое и самое маленькое и среднее арифметическое
# spisok = []
# spisok.extend([int(input("Enter num1: ")), int(input("Enter num2: ")), int(input("Enter num3: ")), int(input("Enter num4: ")), int(input("Enter num5: "))])
# spisok.sort() 
# spisok.sort(reverse=True) 
# avr = sum(spisok) / len(spisok)

# print("Отсортированный список:", spisok)
# print("Среднее значение:", avr)



# № 3
# создайте пременное 
# products = [
#   'яблоко', 
#   'груша', 
#   'арбуз',
#   'банан', 
#   'мандарин'
# ]
# распечатайте его на экране 
# пусть пользователь быверит индекс товара
# после удалите товар из products
# если пользователь ввел индекс которого нет 
# скажите что он не правильно ввел индекс


# products = [
#   'яблоко', 

#   'груша', 

#   'арбуз',

#   'банан', 

#   'мандарин'
# ]

# choose = int(input("Enter index from 0 - 4: "))
# lenghind = len(products)
# if 0 <= choose < lenghind:
#     del products[choose]
#     print(products)
# else:
#     print("Out of index range")





# № 4
# тест
# создайте переменный points = 0
# спросите у пользователя вопрос с 3 ответами  
# если пользователь выберит правильный вариант тогда в переменный points =  + 1 
# 
# создайте 4 таких вопроса  
# в конце распечатайте points
# в итоге если ответ будет равен или больше 3
# скажите "вы прошли тест"
# а если результат будет равен 1 или 2
# скажите "вы провалили тест попробуйте след раз"
# иначе скажите "вы не от ветили ни на один вопрос"

# points = 0

# # Question 1
# q1 = "1. London is the capital of Great Britain?"
# print(q1)
# options = input("Enter yes, no, or don't know: ")
# opt1 = "yes"
# opt2 = "no"
# opt3 = "don't know"
# if options == opt1:
#     points += 1
#     print("Go next")
# else:
#     print("Go next")

# # Question 2
# q2 = "2. Is the sun a star?"
# print(q2)
# options = input("Enter yes, no, or don't know: ")
# if options == opt1:
#     points += 1
#     print("Go next")
# else:
#     print("Go next")

# # Question 3
# q3 = "3. Is water made up of two hydrogen atoms and one oxygen atom?"
# print(q3)
# options = input("Enter yes, no, or don't know: ")
# if options == opt1:
#     points += 1
#     print("Go next")
# else:
#     print("Go next")

# # Question 4
# q4 = "4. Is the Earth flat?"
# print(q4)
# options = input("Enter yes, no, or don't know: ")
# if options == opt2:
#     points += 1

# print("Total points:", points)
# if points == 0 or points == 1 or points == 2:
#     print("u did not pass")
# elif points == 3 or points == 4:
#     print("U passed")
# № 5
# создайте лист с длиной 10 значений  
# спросите у пользователя цифру от одного до 9
# выведите ему лист от числа которого он вел до конца


# my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# indexnum = int(input("Enter from 1-9: "))
# print(my_list[indexnum:])


# № 6
# Подтверждения пароля 
# спросите у пользователя логин и пароль и подтверждения пороля
# создайте условие где проверяется логин он должен состоять и из цифр и из букв. пример 'aktan2002' (используйте isdigit() и isaplha() для проверки)
# cоздайте условие где проверяется пароль он должен совпадать с подтверждением пароля
# если пройдет все проверки тогда сохраните в списке users. пример users = [('aktan2002', 'qwerty'),('ilim12', '12345')]

# users = []
# log = input("Enter log: ")
# if not log.isdigit() and not log.isalpha():
#     log2 = (input("Enter log one more time: "))
#     if log2 == log:
#         users.append(log)
#         print("Succesfull with log")
#         key = input("Enter key: ")
#         if not key.isdigit() and not key.isalpha():
#             key2 = (input("Enter key one more time: "))
#             if key2 == key:
            
#                 users.append(key)
#             print("Succesfull with key")
#         else:
#             print("Keys are not equal")

#     else:
#         print("Key should consist of digits and alphas, try one more time")
#     print(users)
    
# else:
#     print("Logs are not equal, try one more time")

    


