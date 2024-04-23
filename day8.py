# set = {1,2,3}
# dict = {"Key": "value", "key2:": "value2"}



# float = 3.14
# int = 213
# str = ''
# bool = True
# list = []
# tuple = ()

# set = {1, 2, 3}
# dict = {'key': 'value', 'key2': 'value2'}


# # dict = list

# list = ['Ali', 21, 'Tashkent',True, 'developer',['football', 'guitar', 'coding'],]



# dict = {
#         'name': 'Ali' , 
#         'age': 21,
#         'city': 'Tashkent',
#         'is_married': True,
#         'profession': 'developer',
#         'hobbies': ['football', 'guitar', 'coding'],
#     }

# dict ['languages'] = ['Russian', 'English']
# dict2 = {'car': True}

# dict.update(dict2) # добавляет в словарь другой словарь
# print('has car' if dict['car'] else 'no car')

# dict.update(cat = 'black') # добавляет в словарь ключ и значение
# print(dict)

# dict.pop('age') # удаляет ключ и значение из словаря
# print(dict)

# print(dict.get('age')) # получает значение ключа

# dict['age'] = 24
# print(dict.get('age')) # получает значение ключа

# print(dict.keys()) # получает ключи словаря
# print(dict.values()) # получает значения словаря

# for i in dict.keys():
#     print(dict.get(i),i)

# key,value = ('name','Alan')
# print(key, value)

# set = {5, 6, 1, 1, 7 ,9 ,4 , 3, 4, 5, 6, 7, 8, 9, 10, 15, 20, 101}
# print(set)

# names = ["Bek", "Isa", "Ali", "Akan", "Temirlan", "Ali", "Bek", "Isa", "Ali", "Akan", "Temirlan", "Ali"]
# print(names)
# names = list(set(names))
# print(names)    

# set1 = {1, 2, 3, 4, 5, "a", "b", "c"}
# set2 = {1, 2, 3, 4, 5}
# print(set1.difference(set2))
# print(set2.difference(set1))
# print(set1.intersection(set2))
# print(set2.intersection(set1))

# set = {"d", 1, 2, 3, 4, 5, "a", "b", "c"}
# set.add("f")
# print(set)
# set.update(["g", "h"])
# print(set)
# set.remove("d")
# print(set)
# set.pop()
# print(set)
# set.discard("a")
# print(set)
# set.remove(7)
# print(set)



# for key, value in dict.items():
#     print(key, value)

# print(dict['age'], dict['name'], dict['city'], dict['is_married'], dict['profession'], dict['hobbies'])
# from pprint import pprint

# print(f'Привет {dict["name"]}, Тебе {dict["age"]} лет, \
#       Ты из {dict["city"]}. Ты \
#         {'Женат' if dict["is_married"] else "Не женат"}. \
#             Твой профессия {dict["profession"]}, \
#                 твои хобби {dict["hobbies"]}')

# users = [
#     {
#         'name': 'Ali' , 
#         'age': 21,
#         'city': 'Tashkent',
#         'is_married': True,
#         'profession': 'developer',
#         'hobbies': ['football', 'guitar', 'coding'],
#         },
#     {
#         'name': 'Ali' , 
#         'age': 21,
#         'city': 'Tashkent',
#         'is_married': True,
#         'profession': 'developer',
#         'hobbies': ['football', 'guitar', 'coding'],
#         },
#     {
#         'name': 'Ali' , 
#         'age': 21,
#         'city': 'Tashkent',
#         'is_married': True,
#         'profession': 'developer',
#         'hobbies': ['football', 'guitar', 'coding'],
#         }
# ]



# SET

# 1. Попросите пользователя ввести 10 чисел и выведите только уникальные из них.
# c = set()
# for i in range(4):
#     num = int(input("Enter nums"))
#     c.add(num)
#     print(c)


# 2. Создайте два множества из случайных чисел от 1 до 10 каждое и выведите их пересечение.
# stlist = {1,7,9,4,6,8,4}
# ndlist = {6,7,9,4,5,1,5,7}
# inter = stlist.intersection(ndlist)
# print(inter)


# 3. Заполните множество числами от 1 до 10, а затем удалите из него все четные числа.

# nums = {6,7,9,4,5,1,5,7}
# lis = nums.copy()
# for i in lis:
#     if i % 2 == 0:
#         nums.remove(i)
# print(lis)

# 4. Создайте множество, содержащее все буквы алфавита, и затем удалите гласные буквы из него.
# Список гласных букв на английском
# vowels = {'a', 'e', 'i', 'o', 'u'}

# # Список алфавита на английском
# alphabet = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
#             'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'}
# alphabetnovow = alphabet.difference_update(vowels)
# print(alphabet)




# 5. Попросите пользователя ввести несколько чисел, разделенных пробелом, и выведите их в упорядоченном виде без повторений.
# Запросить у пользователя ввод чисел, разделенных пробелом
# input_numbers = input("Введите несколько чисел, разделенных пробелом: ")

# # Разбить строку на отдельные числа
# numbers_list = input_numbers.split()

# # Преобразовать числа в целочисленный тип данных
# numbers_set = set(map(int, numbers_list))

# # Преобразовать множество обратно в список и отсортировать его
# sorted_numbers = sorted(numbers_set)

# # Вывести упорядоченный список чисел без повторений
# print("Упорядоченные числа без повторений:", sorted_numbers)



# print(c)




# 6. Создайте два множества, содержащих кубы чисел от 1 до 5 и от 4 до 8 соответственно, и найдите их объединение.

# set1 = {x**3 for x in range(1, 6)}
# set2 = {x**3 for x in range(4, 9)}

# union_set = set1 | set2
# print(union_set)

# 7. Создайте множество, содержащее все простые числа до 20, и найдите их сумму.

# primes = set()
# for num in range(2, 21):
#     if all(num % i != 0 for i in range(2, int(num ** 0.5) + 1)):
#         primes.add(num)

# primes_sum = sum(primes)
# print("Простые числа до 20:", primes)
# print("Сумма простых чисел:", primes_sum)



# 8. Создайте множество, содержащее буквы из предложения "Quick brown fox jumps over the lazy dog", и найдите количество гласных букв в нем.

# sentence = "Quick brown fox jumps over the lazy dog"
# vowels = {'a', 'e', 'i', 'o', 'u'}
# letters = set(sentence.lower())  
# vowel_letters = letters.intersection(vowels)

# num_vowels = len(vowel_letters)  

# print("Множество букв в предложении:", letters)
# print("Количество гласных букв в предложении:", num_vowels)


# 9. Создайте множество, содержащее все цифры от 0 до 9, и найдите их разность с множеством чисел от 1 до 5.


# all_digits = set(range(10))
# numbers_1_to_5 = set(range(1, 6))
# difference = all_digits - numbers_1_to_5

# print("Множество всех цифр от 0 до 9:", all_digits)
# print("Множество чисел от 1 до 5:", numbers_1_to_5)
# print("Разность множеств:", difference)


# 10. Создайте множество, содержащее уникальные символы из строк "hello" и "world", и найдите его длину.


# unique_characters = set("hello") | set("world")

# length = len(unique_characters)

# print("Множество уникальных символов:", unique_characters)
# print("Длина множества:", length)



# 1. Создайте словарь, представляющий информацию о студентах, где ключом будет идентификатор студента (например, номер студенческого билета), а значением - словарь с данными о студенте (имя, возраст, средний балл и т. д.).
# students_info = {
#     101: {'name': 'Иван', 'age': 20, 'average_score': 4.5},
#     102: {'name': 'Мария', 'age': 22, 'average_score': 4.2},
#     103: {'name': 'Алексей', 'age': 21, 'average_score': 4.8}
# }


# 2. Напишите функцию, которая принимает на вход словарь с данными о студентах и возвращает список имен студентов.

# students_info = {
#     101: {'name': 'Иван', 'age': 20, 'average_score': 4.5},
#     102: {'name': 'Мария', 'age': 22, 'average_score': 4.2},
#     103: {'name': 'Алексей', 'age': 21, 'average_score': 4.8}
# }

# student_names = [student_info['name'] for student_info in students_info.values()]

# print(student_names) 




# 3. Реализуйте функцию для вычисления среднего возраста студентов на основе словаря с данными о студентах.

# students_info = {
#     '1': {'name': 'Alice', 'age': 20},
#     '2': {'name': 'Bob', 'age': 22},
#     '3': {'name': 'Charlie', 'age': 21}
# }

# total_age = 0
# num_students = len(students_info)

# for info in students_info.values():
#     total_age += info['age']

# average_age = total_age / num_students if num_students != 0 else 0

# print("Средний возраст студентов:", average_age)




# 4. Напишите программу для объединения двух словарей с данными о студентах, представленных разными группами.

# group1 = {
#     '1': {'name': 'Alice', 'age': 20},
#     '2': {'name': 'Bob', 'age': 22}
# }

# group2 = {
#     '3': {'name': 'Charlie', 'age': 21},
#     '4': {'name': 'David', 'age': 23}
# }

# group1.update(group2)
# print(group1)





# 5. Создайте словарь, содержащий информацию о количестве различных букв в строке (ключ - буква, значение - количество раз, которое она встречается).
# text = "Hello, World!"

# letter_count = {}

# for char in text:
#     if char.isalpha():  # Проверяем, является ли символ буквой
#         char = char.lower()  # Приводим символ к нижнему регистру
#         if char in letter_count:
#             letter_count[char] += 1  # Увеличиваем счетчик для текущей буквы
#         else:
#             letter_count[char] = 1  # Инициализируем счетчик для новой буквы

# print(letter_count)






# 6. Напишите функцию для удаления определенного элемента из словаря по ключу.


# my_dict = {'a': 1, 'b': 2, 'c': 3}
# print("Исходный словарь:", my_dict)

# key_to_remove = 'b'
# if key_to_remove in my_dict:
#     del my_dict[key_to_remove]
#     print(f"Элемент с ключом '{key_to_remove}' удален из словаря.")
# else:
#     print(f"Элемент с ключом '{key_to_remove}' не найден в словаре.")

# print("Словарь после удаления элемента:", my_dict)




# 7. Реализуйте программу для объединения нескольких словарей в один.
# dict1 = {'a': 1, 'b': 2}
# dict2 = {'b': 3, 'c': 4}
# dict3 = {'d': 5}

# merged_dict = {**dict1, **dict2, **dict3}

# print(merged_dict)





# 8. Создайте словарь, содержащий информацию о покупках в магазине (название товара - ключ, количество купленных единиц - значение).

# purchases = {
#     'apple': 5,
#     'banana': 3,
#     'orange': 2,
#     'milk': 1,
#     'bread': 2
# }

# print(purchases)





# 9. Напишите функцию для поиска наибольшего значения в словаре.

# покупки = {'яблоко': 5, 'банан': 3, 'апельсин': 2, 'молоко': 1, 'хлеб': 2}
# максимальное_значение = max(покупки.values())
# print("Наибольшее количество купленных единиц:", максимальное_значение)






# 10. Создайте словарь, представляющий граф смежности для некоторого графа, где ключ - вершина, а значение - список смежных вершин.




# listofproducts = []

# while True:
#     print("Меню:")
#     print("1. Создать список ингредиентов")
#     print("2. Удалить ингредиент")
#     print("3. Показать список ингредиентов")
#     print("4. Выйти из программы")

#     action = input("Выберите действие: ")

#     while action == '1':
#         ingr = input("Введите название ингредиента: ")
#         listofproducts.append(ingr)
#         print(f"Ингредиент {ingr} добавлен в список.")

        
#     if action == '2':
#         ingr = input("Введите название ингредиента, который хотите удалить: ")
#         if ingr in listofproducts:
#             listofproducts.remove(ingr)
#             print(f"Ингредиент {ingr} удален из списка.")
#         else:
#             print(f"Ингредиент {ingr} не найден в списке.")
#     elif action == '3':
#         print("Список ингредиентов:")
#         for ingr in listofproducts:
#             print(ingr)
#     elif action == '4':
#         print("Выход из программы.")
#         break
#     else:
#         print("Некорректный ввод. Пожалуйста, выберите действие снова.")
