# def func(x):
#     y = x+3
#     return y
# print(func(7))

# def - key word for creating function
# func - name of function
# return - 


# def well(x):
#     #your code here
#     return ''

# def well(x):
#     count = 0
#     for i in x:
#         if i == "good":
#             count += 1

#     if count == 1 or count == 2:
#         return "Publish!"
#     if count == 0:
#         return "Fail!"
#     else:
#         return "I smell a series!"



# print(well(['bad', 'bad', 'bad']) == 'Fail!')
# print(well(['good', 'bad', 'bad', 'bad', 'bad']) == 'Publish!')
# print(well(['good', 'bad', 'bad', 'bad', 'bad', 'good', 'bad', 'bad', 'good']) == 'I smell a series!')

# Напишите функцию, которая принимает на вход целое число и возвращает количество битов, равных единице в двоичном представлении этого числа. Вы можете гарантировать, что ввод неотрицательный.

# Пример : двоичное представление 1234is , поэтому в этом случае 10011010010функция должна вернуть результат.5

# def count_bits(n):
#     count = 0
#     n >= 0
#     n = bin(n)
#     n = str(n)
#     for i in n:
#         if i == "1":
#             count += 1
#     return count

# print(count_bits(0))
# print(count_bits(4))

# print(count_bits(7))
# print(count_bits(9))
# print(count_bits(10))


# even or odd done




# def digital_root(n):
#     sums = sum([int(num) for num in str(n)])
#     if len(str(sums)) >= 2:
#         sums = digital_root(sums)
#     return sums
# print(digital_root(942))

# def sum_ab(a,b):
#     return a+b
# print(sum_ab(4,5))

# from math import pi
# def square_circle(r):
#     return pi*(r**2)
# print(square_circle(2))  


# def even(n):
#     l = []
#     for i in range(n):
#         if i%2 == 0:
#             l.append(i)
#     return l 
# print(even(100))




# list1 = [-10,5,15,-7,0,57,69,45,12]
# def sum_l(a):
#     l2 = 0
#     for i in a:
#         l2 += i
#     return l2
# print(sum_l(list1))

# def palindrom(a):
#     return a == a[::-1]
# print(palindrom("lola"))
    

# stock = {
#     "t-shirt": 4,
#     "trousers": 8,
#     "shoes": 12,
#     "suit": 7
# }

# def check_value(stock, merch,n):
#     if merch in stock:
#         if n <= stock[merch]:
#             return True
#     return False
    
# print(check_value(stock, "t-shir", 2))


# a = [1,2,7,9,4,6,4,24,38]
# def sum_avr(a):
#     return sum(a)/len(a)
# print(sum_avr(a))



# Таракан – одно из самых быстрых насекомых. Напишите функцию, которая 
# принимает скорость в км в час и возвращает ее в см в секунду, округляя до целого 
# числа (= пол).
# Например:
# 1.08 --> 30
# Примечание! Ввод представляет собой действительное число (фактический тип зависит
# от языка) и >= 0. Результатом должно быть целое число.


# 10 km h = 1 000 000 sm 3600s
# def convert(a):
#     return round(a*100000/3600)
# print(convert(1.08))


# def is_it_letter(s):
#     s = str(s)
#     if s.isalpha():
#         return True 
#     else:
#         return False
# print(is_it_letter("asdja"))

# def is_it_letter(s):
#     return s.isalpha()
# print(is_it_letter("56154"))



# def add(lst):
#     l = []
#     for i in range(len(lst)):
#         l.append(sum(lst[:i+1]))
#     return l
# print(add([1,2,4,9]))



# def add(lst):
#     c=0
#     l = []
#     for i in lst:
#         c += i
#         l.append(c)
#     return l
# print(add([1,2,4,9]))

# def sum(x,y):
#     return x+y
# def divide(x,y):
#     return sum(x,y)/y
# print(divide(6,3))


# vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
# def count_vowels(a):
#     return sum([1 for i in a if i in vowels])
#     # count = 0
#     # for i in a:
#     #     if i in vowels:
#     #         count +=1
#     # return count
# print(count_vowels("jsabdj sakdnad"))


# def oven(n):
#     return [i for i in range(n) if i%2 == 0]
    # ov = []
    # for i in range(n):
    #     if i % 2 == 0:
    #         ov.append(i)
    # return ov
# print(oven(11))

# def oven(n):
#     return [True if i%2 == 0 else False for i in range(n) ]
# print(oven(11))


# from random import randint
# def rnd(n):
#     return [randint(1,n) for i in range(n) ]
#     # b = []
#     # for i in range(n):
#     #     a = randint(1,n)
#     #     b.append(a)
#     # return b
# print(rnd(100))

# a = [4,8,7,6,7,1,23,4]

# Создаем переменную = [Значение которое хотим добавить, цикл фор, условие]
    
