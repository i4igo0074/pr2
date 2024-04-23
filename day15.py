# Аргументы функции могут быть 3 видов:
# 1) обязательные аргументы - функция не будет работать если их не передавать
# 2) аргументы по умолчанию - функция будет работать и если их не передать он возьмет значения 
# которую вы указали по умолчанию
# 3)args, kwargs - они могут получать любое кол-во аргументов
# args - они будут записаныт в виде кортежа(tuple)
# kwargs - они будут записаны в виде словаря(dict)

# def func(*args, **kwargs): #название аргумента тут не имеет значения, главное кол-во звезд
#     print("args=", args)
#     print("kwargs=", kwargs)
# print(func(1,2,3, a=1,b=2,c=3))

# def add(a, b):
#     return a+b

# def sen(a):
#     count = 0
#     for i in a:
#         count += 1
#     return count
# print(sen("nsajdn asjdnasd"))


# def func(**b):
#     a = {"name": "Isa",
#      "name2": "Alan",
#      "name3":"Bektur"
#     }
#     a.update(b)
#     return a
# print(func(id=1,id2=2,id3=3))

# def ord(food, drink):
    
#     with open ("/home/islambek/Рабочий стол/menu.txt", "w") as file:
#         return file.write(f"My food: {food}, your drink: {drink}")
# print(ord("ice-cream", "coke"))

# def open_menu():
#     with open("/home/islambek/Рабочий стол/menu.txt", "r") as file:
#         return file.read()
# print(open_menu())


# def cr_f(n):
#     with open(f"{n}.txt", "w") as file:
#         file.write('test')
# print(cr_f("isa"))



# square = (lambda a: a ** 2)(5)
# print(square)

# a = map(lambda x: x ** 2, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# print(list(a))

# def fil(x):
#     if x % 2 == 0:
#         return True
#     return False

# a = filter(fil, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# a = filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# print(list(a))


# a = [('Январь', 31), ('Февраль', 29),  ('Март', 31), ('Апрель', 30), ('Май', 31), ('Июнь', 30), ('Июль', 31), ('Август', 31)]
# aa = [31, 29,31, 30, 31 ,30 ,31, 31]
# print(aa[3])

# print(sum(aa))

# print(sorted(a, key=lambda x: x[0]))
# print(sum(map(lambda x: x[1], a)))




# g = {'h': 400, 'h': 900}

# print(g['h'])

# data = [{'name': 'Alice', 'age': 30},
#         {'name': 'Bob', 'age': 25},
#         {'name': 'Carl', 'age': 35}]


# def sort(x):
#     return x["name"]
# print(sorted(data, key=sort))

# print(sorted(data, key=lambda x: x['name']))

# 1. Напишите lambda функцию, которая принимает на вход два числа и возвращает их сумму. 
# sumab = lambda a, b: a+b
# print(sumab(4,4))


# 2. Создайте список чисел от 1 до 10. Используйте lambda функцию для возведения каждого числа в этом 
# списке в квадрат.
# nums = list(range(1,11))
# squared_nums = list(map(lambda x: x**2, nums))
# print(squared_nums)


# 3. Дан список слов. Отсортируйте его в алфавитном порядке с использованием lambda функции.
# a = ["samda", "sadmdas", "nfdbfs", "assak", 'osdal', 'ysdksa']
# srt = sorted(a, key=lambda x: x.lower())
# print(srt)



# 4. Создайте список из чисел от 1 до 10. Используйте lambda функцию для фильтрации списка так, 
# чтобы в нем остались только четные числа.

# a = list(range(1,11))
# srt = list(filter(lambda x: x%2==0, a))
# print(srt)
           


# 5. Напишите lambda функцию, которая принимает на вход строку и возвращает ее длину.

# length = lambda s: len(s)
# a = length("as as")
# print(a)


# 6. Дан список чисел. Используйте lambda функцию, чтобы найти наибольшее число в списке.

# a = list(range(1,11))
# mx = lambda x: max(x)
# print(mx(a))


# 7. Создайте список кортежей, где каждый кортеж содержит имя и возраст человека. 
# Отсортируйте этот список по возрасту с использованием lambda функции.
# people = [("Alice", 30), ("Bob", 25), ("Carl", 35)]
# srt  = sorted(people, key=lambda x: x[0]) #why if we use x[0][1] for sorting in rising, how it works?
# print(srt)

# 8. Напишите lambda функцию, которая принимает на вход строку и возвращает ее в обратном порядке.
# x = lambda s: "".join(reversed(s))
# a = "asdm als"
# print(x(a))

# 9. Дан список слов. Используйте lambda функцию, чтобы отфильтровать слова длиной менее 5 символов.
# words = ["apple", "banana", "orange", "grape", "melon", "kiwi", "pear", "fig", "pineapple"]
# srt = list(filter(lambda x: len(x)<5, words))
# print(srt)
# 10. Создайте список из чисел от 1 до 100. Используйте lambda функцию, чтобы найти сумму всех 
# чисел в списке.
# l1 = list(range(101))
# sm = lambda x: sum(x)
# print(sm(l1))

# Создайте 2 функции где одна функция вложена в другую. Главная функция должна выводить на экран 
# текст: "Я главная функция". А вложенная функция должна выводить на экран: "Я вложенная функция."

# def a():
#     print("I am main")
#     def b():
#         print("I am extra")
#         return 'U won'
#     return b()
# print(a())




# Создайте функцию которая принмает тип данных dictionary, но возвращает два Tuple в одном из них все 
# ключи, в другом только значения.
# def process_dictionary(d):
#     keys_tuple = tuple(d.keys())
#     values_tuple = tuple(d.values())
#     return keys_tuple, values_tuple


# my_dict = {"a": 1, "b": 2, "c": 3}
# keys, values = process_dictionary(my_dict)
# print("Keys:", keys)
# print("Values:", values)

def main(data: dict):
    return tuple(data.keys()), tuple(data.values)


# Напишите программу которая определяет ПРОСТЫЕ ЧИСЛА. Простое число - это число которое делится только 
# на себя и на 1.
# def is_prime(num):
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             return "Not simple"
#     return "Yeah, simple"
# print(is_prime(3))




# Напишите функцию которая принимает 2 аргумента. Эти аргументы могут быть любого типа данных но функция
# должна Вам вернуть эти аргументы как тип данных List.
# Напишите функцию которая спрашивает у пользователя число и выводит ему на экран именно столько строк 
# самой себя как текст.
# Создайте функцию которая принимает Имя пользователя и его зарплату и возвращает это строкой 
# как: ИМЯ - ЗАРПЛАТА. Если в функции не была указана зарплата - подставьте её сами. Значение по 
# умолчанию - 5000.
# Напишите функцию которая спрашивает число N и генерирует вам List состоящий из N разных элементов.