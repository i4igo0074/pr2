
"""1. Задачи на переменные и типы данных:
Создайте переменные для хранения имени, возраста, роста и веса человека. Укажите для каждой переменной подходящий тип данных.
Присвойте переменным значения, соответствующие реальному человеку.
Выведите значения всех переменных на экран.
Измените значение переменной age на новое значение.
Выведите на экран сообщение, содержащее имя и возраст человека.
"""

name = " Isa "
age = 24
weight = 67
age = 25

print(name, age, weight)
print(name, age)

""" Задачи на операторы сравнения:
Сравните два числа (например, 10 и 20) с помощью операторов ==, !=, >, <, >=, <=. Выведите результат каждого сравнения на экран.
Сравните две строки (например, "Hello" и "world") с помощью операторов == и !=. Выведите результат каждого сравнения на экран.
Сравните переменную age с 18, используя оператор >=. Выведите на экран сообщение, indicating whether the person is an adult.
"""
print (10 == 20)
print (10 >= 20)
print (10 !=20)

print ("Hello" == "World")
print ("Hello" != "World")

if age >= 18:
    print ("indicating whether the person is not  an adult")
else:
    print ("indicating whether the person is an adult")
"""
Задачи на арифметические операции:
Вычислите сумму, разность, произведение и частное двух чисел (например, 10 и 20).
Возведите число (например, 5) в степень (например, 2).
Найдите остаток от деления одного числа (например, 12) на другое (например, 5).
Решите задачу на вычисление площади прямоугольника, зная его длину и ширину.
Решите задачу на вычисление объема куба, зная его длину ребра."""

print (10*20)
print (5 ** 2)
print (12%5)
a=3
b=4
print(a*b)
print(a ** 3) 

"""
Дополнительные задачи:
Напишите программу, которая запрашивает у пользователя два числа, а затем выводит на экран их сумму, разность, произведение и частное.
Напишите программу, которая запрашивает у пользователя имя и возраст, а затем выводит на экран приветствие, indicating whether the person is an adult.
Напишите программу, которая конвертирует температуру из градусов Цельсия в градусы Фаренгейта.
Напишите программу, которая вычисляет площадь круга, зная его радиус.
"""
a = int(input("Enter the first number: "))
print ("Cool, now enter second number")
b = int(input())
print(a-b, a*b, a/b)


name = input("Enter your name: ")
age = int(input("Enter your age: "))
if age >= 18:
    print ("Hello, ndicating whether the person is an adult")
else:
    print("Hello, ndicating whether the person is not an adult")


celsiustofahrenheit = int(input("Enter number in  Celcius: "))
fahrenheit =  (celsiustofahrenheit * 9/5) + 32

print(fahrenheit)


import math


r = float(input("Enter radius of circle: "))
areaofsquare = math.pi * (r ** 2)
print("Area of square equal to", areaofsquare)

