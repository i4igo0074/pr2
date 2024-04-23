# try: except: 

# try:
#     a = int(input("Enter a number: "))
#     print(10 / a)
# except ValueError:
#     print("Invalid input, Введите цифру пожалуста!")
# except ZeroDivisionError:
#     print("На ноль делить нельзя!")
# else:
#     print("Успешно!")
# finally:
#     print("Конец программы!")


# s = input(

# try:
#     print(1 + '2')
# except TypeError as e:
#     print('Ошибка типа', e)

# try:
#     print(5 // 0)
# except ZeroDivisionError as e:
#     print("Деление на ноль!", e)

# try:
#     if 1 % 2 == 0:
#      print(1)
# except SyntaxError:
#     print('Ошибка табуляции')


# try:
#     a = [1, 2, 3]
#     print(a[3])
# except IndexError:
#     print('Неверный индекс')


# a = [1, 2, 3]
# i = 0

# while True:
#     try:
#         print(a[i])
#     except IndexError:
#         break
#     i += 1

# numbers = [1, 2, 3]
# numbers.remove('hello')  # ValueError: list.remove(x): x not in list

# set = {312,123,123,123}
# set.remove(123)

# values = ("Razakov 32", 10, 1005, ["tables", "chairs"], 23.00)
# asc = []

# for i in values:
#     try:
#         s = set(i)
#         asc.append(True)
#     except TypeError:
#         asc.append(False)
    



# fruits = ['яблоко', 'груша', 'апельсин'] 

# while True:
#     try:
#         n = int(input('Введите индекс фрукта: '))
#         print(fruits[n])
#     except IndexError:
#         print('Неверный индекс, Такой фрукт  не найден')
#     except ValueError:
#         print('Введите целое число')
#     except KeyboardInterrupt:
#         print('Выход')
#         break



# print(len(1))

# print(a)

# a = {
#     'name': 'Alan'
# }
# print(a['age'])


# a = open('day19.txt', 'r')
# print(a.read())

# try:
#     dict_ = {'name': 'john', 'lastname': 'Snow', 12: 'age', 'surname': 'john'}

#     for x in dict_.keys():
#         print(x + 'abc')

# except TypeError:
#     print('Ошибка типа')


# dict_ = {'name': 'john', 'lastname': 'Snow', 12: 'age', 'surname': 'john'}

# for x in dict_.keys():
#     try:
#         print(x + ' abc')
#     except TypeError:
#         print('Ошибка типа')


# 1 Написание кода, который открывает файл, читает его содержимое и затем закрывает его. Можно использовать блок try-except для перехвата любых ошибок, 
# которые могут возникнуть, если файл не существует или есть проблемы с чтением файла.
# try:
#     with open("programming/python/data.txt", "r") as file:
#         print(file.read())
# except Exception as e:
#     print("smthng Error", e)



#  2 Разбор ввода пользователя, чтобы убедиться, что он находится в правильном формате. Например, если пользователю предлагается ввести дату, 
# можно использовать try-except для перехвата ошибок, если ввод не находится в правильном формате.




# from datetime import datetime

# user_input = input("Введите дату в формате ДД.ММ.ГГГГ: ")

# try:
#     datetime.strptime(user_input, "%d.%m.%Y")
#     print("Дата введена в правильном формате: ДД.ММ.ГГГГ")
# except ValueError:
#     print("Ошибка: Неверный формат даты. Пожалуйста, введите дату в формате ДД.ММ.ГГГГ")



#  3 Подключение к удаленному серверу или API. Если возникают проблемы с подключением, можно использовать блок try-except для обработки ошибок и 
# предотвращения аварийного завершения программы.
# import requests

# try:
#     response = requests.get("https:/api.example.c")
#     if response.status_code == 200:
#         print("Успешно подключено к серверу")
#     else:
#         print(f"Ошибка при подключении: {response.status_code}")
# except requests.ConnectionError:
#     print("Ошибка: Не удается подключиться к серверу")
# except requests.Timeout:
#     print("Ошибка: Превышено время ожидания подключения")
# except requests.RequestException as e:
#     print(f"Ошибка при выполнении запроса: {e}")


#  4 Написание кода, который взаимодействует с базой данных. Использование try-except может помочь перехватывать ошибки, которые могут возникать 
# во время запросов или соединений с базой данных.




#  5 Выполнение математических операций, которые могут привести к ошибкам, например, деление на ноль или извлечение квадратного корня из отрицательного числа.

# import math

# try:
#     num1 = float(input("Enter num: "))
#     num2 = float(input("Enter num: "))
#     option = input("Enter +, -, *, /, sqrt: ")
    
#     if option == '+':
#         print(num1 + num2)
#     elif option == '-':
#         print(num1 - num2)
#     elif option == '*':
#         print(num1 * num2)
#     elif option == '/':
#         if num2 == 0:
#             print("You can't divide by zero")
#         else:
#             print(num1 / num2)
#     elif option == 'sqrt':
#         if num1 < 0 or num2 < 0:
#             print("Negative value can't be used for square root")
#         else:
#             print(f'{math.sqrt(num1), math.sqrt(num2)}')
#     else:
#         print("Invalid option")
# except ValueError:
#     print("Invalid input. Please enter valid numbers")


#  6 Запуск кода, который включает внешние библиотеки или пакеты. Если внешний пакет не установлен или есть проблемы с пакетом, можно использовать 
# try-except для обработки ошибок.





#  7 Написание кода, который отправляет электронную почту или другие типы сообщений. Если возникают проблемы с процессом отправки сообщений, можно использовать блок try-except для обработки ошибок и предотвращения аварийного завершения программы.





#  8 Разбор или парсинг данных с веб-страниц. Использование try-except может помочь перехватывать ошибки, которые могут возникать, если есть проблемы с веб-сайтом, с которого извлекаются данные, или если данные имеют неправильный формат.





#  9 Написание кода, который взаимодействует с внешним оборудованием или устройствами. Если возникают проблемы с подключением к оборудованию или устройству, можно использовать блок try-except для обработки ошибок.





#  10 Создание системы обработки ошибок по индивидуальному заказу. Можно использовать try-except для перехвата конкретных типов ошибок и затем обрабатывать их таким образом, чтобы это имело смысл для вашего