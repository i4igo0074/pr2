# def decor(n):
#     print("I am decor")
#     def inner ():
#         print("I am inner")
#         return n ** 2
#     return inner()
# print(decor(5))

# def decor(func):
#     print("1")
#     def inner():
#         print("2")
#         result = func()
#         print("3")
#         return result
#     print("4")
#     return inner
# @decor
# def hello():
#     print("5")
#     return "Hello"
# print("6")
# print(hello())
# print("7")


# import time
# from random import randint

# def timer(func):
#     def wrapper(n):
#         start = time.time()
#         result = func(n)
#         end = time.time()
#         print(f'Time: {end - start}')
#         return result
#     return wrapper
# @timer
# def func(n):
#     print([randint(1,n) for _ in range(n)])
# func(10000)

# import time
# from random import randint

# def timer(func):
#     def wrapper(n):
#         start = time.time()
#         result = func(n)
#         end = time.time()
#         print(f'Time: {end - start}')
#         return result
#     return wrapper
# def unique(func):
#     def wrapper(n):
#         result = func(n)
#         return list(set(result))
#     return wrapper

# def sort(func):
#     def wrapper(n):
#         result = func(n)
#         return sorted(result)
#     return wrapper

# @timer
# @sort
# @unique

# def func(n):
#     return([randint(1,1000) for _ in range(n)])
# print(func(10))


# def decor(func):
#     print("Hello i'm decor!")
#     def inner():
#         print("Hello i'm inner!")
#         result = func()
#         print(result)
#         print("Bye!")
#         return result
#     return inner

# @decor
# def hello():
#     return "Hello"

# print(hello())




# def decor(func):
#     print("1")
#     def inner():
#         print("4")
#         result = func()
#         print("6")
#         return result
#     print("2")
#     return inner

# @decor
# def hello():
#     print("5")
#     return "Hello"

# print('3')
# print(hello())
# print('7')




# # def decor(func):
# #     def inner(n, x):
# #         return func(n, x) / 2
# #     return inner

# # @decor
# # def hello(n, x):
# #     return n ** x

# # print(hello(5, 2))


# user_data = {"admin": 1234,
#              "guest": 4567
#              }

# def auth_ent(func):
#     def wrapper():
#         symb = input("Enter rights: ")
#         result = func(symb)
#         return result
#     return wrapper

# @auth_ent
# def check_data(symb):
#     if symb == str(user_data["admin"]):
#         print("U passed")

# check_data()

# user_data = {"admin": 1234}

# def auth_required(func):
#     def wrapper():
#         username = input("Введите имя пользователя: ")
#         password = int(input("Введите пароль: "))
#         if username in user_data and password == user_data.get(username):
#             func()
#         else:
#              print('Нет права доступа')
#     return wrapper

# @auth_required
# def access_protected_data():
#         print('добро пожаловать')
#         return 

# access_protected_data()


# data_cache = {
#     4:24,
#     5:120}

# def decor(func):
#     def wrapper(n):
#         if n in data_cache:
#             return data_cache[n]
#         result = func(n)
#         data_cache[n] = result
#         return result
#     return wrapper
        

# @decor
# def calc_fac(n):
#     count = 1
#     for i in range(1,n+1):
#         count *= i
#     return count


# print(calc_fac(5))
# print(calc_fac(15))
# print(calc_fac(15))



# def dec(func):
#     def wrapper(*args, **kwargs):

#         print("func is started")
        
#         result = func(*args,**kwargs)
#         print(f"res={result}")
#         print("Is finished")  
#         return result
#     return wrapper

# @dec
# def add(a,b):
#     return a + b
    
    
# add(3,5)


