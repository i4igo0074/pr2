# list = [1,2,3,4, [1,2,3,[23]]]
# s = list[4]
# print(s)
# b = s[3]
# print(b)
# c = b[0]
# print(c)



# for
# while
# pros = "asdnmdksg"
# for i in pros:
#     print(i)

# nums = list(range(1, 101))
# count = 0
# for i in range(1, 100):
#     if i % 2 != 0:
#         print(i)
#         count += i

# print(count)

# a = 5
# for i in range(1, 11):
#     print(f'5 * {i} = {a*i}')


# list = []
# q = "Enter num: "
# for i in range(1,4):
#     list.append(int(input(q)))

# list.sort()
# print(list)
# print(list[-1])
# print(list[0])

# for a in sorted(list):
#     print(a)

# months = [
#     "Январь",
#     "Февраль",
#     "Март",
#     "Апрель",
#     "Май",
#     "Июнь",
#     "Июль",
#     "Август",
#     "Сентябрь",
#     "Октябрь",
#     "Ноябрь",
#     "Декабрь"
# ]
# # months[0:13:2]
# # print(months)

# # for i in months[::2]:
# #     print(i)

# for i in range(0, 12):
#     if i % 2 != 0:
#         print(months[i])

# Sum til N
# sumn = 0
# n = int(input("Enter from 7-40: "))
# for i in range(0, n+1):
#     sumn += i
# print(sumn)


# for i in range(11):
#     print(f'5*{i} = {5*i}')

# for i in range(11):
#     for b in range(11):
#         print(f'{i} * {b} = {i * b}')


# i = range(1:10:3)
# for h in range(1, 24):
#     for m in range(60):
#         for s in range(60):
#             print(f'{h} : {m} : {s}')
#             print()



# for k in range(1, 10, 3): # [1, 4, 7]
#     for j in range(1, 10):
#         print(f'\t {k} * {j} = {k * j} \
#                 \t {k+1} * {j} = {k + 1 * j} \
#                 \t {k+2} * {j} = {k + 2 * j}')
#     print()

# 1. Вывод чисел:
# 1.1. Вывести все числа от 1 до 100.

# for num in range(1, 101):
#     print(num)

# 1.2. Вывести все четные числа от 1 до 50. 

# for num in range(1,51):
#     if num % 2 == 0:
#         print(num)


# 1.3. Вывести все нечетные числа от 100 до 1. 

# for num in range(101, 1, -1):
#     if num % 2 != 0:
#         print(num)

# 1.4. Вывести все числа от 20 до 35 в обратном порядке.

# for num in reversed(range(20, 36)):
#     print(num)

# 2. Работа со списками:
# 2.1. Найти сумму всех элементов списка. 

# sum = 0
# list1 = [2, 4 , 6, 8, 9]
# for a in list1:
#     sum += a
# print(sum)
    

# 2.2. Найти минимальный и максимальный элемент списка.

# list1 = [10, 4, 6, 8, 9]
# min_value = list1[0]  # Предположим, что первый элемент списка - минимальный
# for num in list1:
#     if num < min_value:
#         min_value = num
# print(min_value)

# 2.3. Вывести все элементы списка, которые больше 10. 

# list1 = [10, 4, 6, 8, 9, 20,25,26]

# for i in list1:
#     if i > 10:
#         print(i)


# 2.4. Удалить из списка все элементы, которые меньше 5.

# list1 = [10, 4, 6, 8, 9, 20,25,26]
# for i in list1:
#     if i < 5:
#         list1.remove(i)
#         print(list1)

# 3. Работа со строками:
# 3.1. Найти длину строки.


# count = -1
# text = "Isa is best player"
# for i in text:
#     count += 1
# print(count)


# 3.2. Вывести строку в обратном порядке. 
# text = "Isa is best player"
# lenth = len(text)
# for i in range(lenth-1, -1, -1):
#     print(text[i])

# text = "Isa is best player"
# length = len(text)
# i = length - 1

# while i >= 0:
#     print(text[i])
#     i -= 1




# 3.3. Найти количество вхождений символа 'a' в строке. 
# text = "Isa is best player"
# count = 0
# for i in text:
#     if i == "a":
#         count += 1
# print(count)


# text = "Isa is best player"
# count = 0
# i = 0

# while i < len(text):
#     if text[i] == "a":
#         count += 1
#     i += 1

# print(count)



# 3.4. Преобразовать строку в верхний/нижний регистр.
# text = "Isa is best player"
# uppertext = ""
# for i in text:
#     uppertext += i.upper()
# print(uppertext)


# text = "Isa is best player"
# uppertext = ""
# i = 0

# while i < len(text):
#     uppertext += text[i].upper()
#     i += 1

# print(uppertext)



# 4. Математические задачи:
# 4.1. Вычислить факториал числа N.
# count = 1
# num = int(input("Enter num: "))
# for i in range(1, num+1):
#     count *= i
# print(count)

# 4.2. Вычислить сумму квадратов первых N чисел. 
# list1 = []
# sum = 0
# for i in range(4):
#     nums = int(input("Enter nums: "))
#     list1.append(nums)
#     print(list1)
    
#     for a in list1[:2]:
#         print(a)
#         sum += a ** 2
# print(sum)




# list1 = []
# sum = 0
# i = 0

# while i < 4:
#     nums = int(input("Enter nums: "))
#     list1.append(nums)
#     print(list1)
    
#     a = 0
#     while a < 2 and a < len(list1):
#         print(list1[a])
#         sum += list1[a] ** 2
#         a += 1
        
#     i += 1

# print(sum)


# 4.3. Найти все простые числа от 1 до N. 

# num = int(input("Enter num: "))
# for i in range(2, num+1):
#     if i % 2 != 0 and i % 3 != 0:
#         print(i)

# i = 2
# num = int(input("Enter num: "))
# while i < num: 
#     for a in range(2, num+1)
#     if i % 2 != 0 and i % 3 != 0:
#         print(i)
#     i += 1

# 4.4. Вычислить значение функции f(x) = x^2 + 3x - 1 для всех x от 1 до 10.


# for i in range (1, 11):
#     fx = (i**2) + 3*i - 1
#     print(fx)


# i = 0
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# while i < len(a):
#     fx = (a[i]**2) + 3*a[i] - 1
#     print(fx)
#     i+= 1


# 5. Задачи на логику:
# 5.1. Определить, является ли число N палиндромом.

# for i in range(10, 100):
#     a = str(i)
#     if a == a[::-1]:
#         print(i)

# for i in range(10, 100):
#     a = str(i)
#     c = 0
#     while c < len(a) and a == a[c::-1]:
#         print(a)
#         c += 1


# 5.2. Найти все делители числа N.
# list1 = []
# n = 8
# for i in range(1, 9):
#     c = n / i
#     if c % n == 0:
#         list1.append(c)
#         print(c)

# N = int(input("Введите число: "))

# print("Делители числа", N, ":", end=" ")
# for i in range(1, N + 1):
#     if N % i == 0:
#         print(i, end=" ")


# 5.3. Определить, является ли треугольник с заданными сторонами прямоугольным. 5.4. Вывести все комбинации из N цифр.

# for a in range(1, 101):
#     for b in range(1, 101):
#         for c in range(1, 101):
          
#             if a**2 + b**2 == c**2:
#                 print(f"Стороны {a}, {b} и {c} образуют прямоугольный треугольник.")


# a = 1
# b = 1
# c = 1

# while a <= 100:
#     while b <= 100:
#         while c <= 100:
#             if a**2 + b**2 == c**2:
#                 print(f"Стороны {a}, {b} и {c} образуют прямоугольный треугольник.")
#             c += 1
#         b += 1
#         c = b
#     a += 1
#     b = a



# 6. Дополнительные задачи:



# 6.1. Нарисовать квадрат с помощью символов '*'. 

# size = 5 

# for i in range(size):
#     for j in range(size):
#         if i == 0 or i == size - 1 or j == 0 or j == size - 1:
#             print('*', end=' ')
#         else:
#             print(' ', end=' ')

#     print()  

# size = 5  # Размер квадрата
# i = 0     # Инициализация переменной для строки

# while i < size:
#     j = 0  # Инициализация переменной для столбца

#     while j < size:
#         # Проверяем, находится ли текущая позиция на грани квадрата или на его угловой точке
#         if i == 0 or i == size - 1 or j == 0 or j == size - 1:
#             print('*', end=' ')  # Выводим символ '*' для внешних граней квадрата
#         else:
#             print(' ', end=' ')  # Выводим пробел для внутренних областей квадрата
#         j += 1  # Переходим к следующему столбцу

#     print()    # Переходим на новую строку после завершения одной строки квадрата
#     i += 1     # Переходим к следующей строке



# 6.2. Вывести таблицу умножения.

# for i in range(1, 11):
#     for j in range(1, 11):
#         print(f"{i}*{j} = {i*j}")

# i = 1
# while i <= 10:
#     j = 1
#     while j <= 10:
#         print(f"{i}*{j} = {i*j}")
#         j += 1
#     i += 1
