# file_name = 'lol/command.sh'

# file = open(file_name, mode='r') 
# print(file.read())

# file = open(file_name, 'r') 
# print(file.read())


# file = open('main.txt', 'w')
# file.write('Hello world')

# file = open('main.txt', 'w')
# file.write('Hello world')

# with open('main.txt', 'r') as file:
#     print(file.read().split()) # выводит весь файл
    # print(file.readline(100)) # выводит первую строку из файла
    # print(file.readlines()) # выводит список строк из файла

# with open('main.txt', 'r') as file:
#     for i in file:
#         print(i)


# with open('main.txt', 'w') as file:
#     file.write('1 Hello world\n')

# with open('main.txt', 'a') as file:
#     file.write('2 Hello world')



# with open('image.jpg', 'rb') as file:
#     x = file.read()
    
#     with open('main.txt', 'wb') as file2:
#         file2.write(x)


# file = open('analyzeslaries.txt', 'w')
# file.write("""Январь 26500000 
# Февраль 300000
# Март 100000000
# Апрель 200000
# Май 3000000
# Июнь 4000000
# Июль 5000000
# Август 6000000
# Сентябрь 7000000
# Октябрь 8000000
# Ноябрь 9000000
# Декабрь 10000000
# """)

# file.close()
# total_salary = 0
# with open("analyzeslaries.txt", 'r') as file:
#     for i in file:
#         month, salary = i.split()
#         total_salary += int(salary)
# print("Общая сумма зарплаты:", total_salary)

# nummm = 0
# with open("analyzeslaries.txt", "r") as file:
#     for i in file:
#         month, salary = i.split()
#         print(month)
#         if month == "Январь" or month == "Май":
#             print(salary)
#             nummm += int(salary)
        
# list1 = {}
# seasons = {
#     "Winter": ["Декабрь","Январь", "Февраль"], 
#     "Spring": ["Март", "Апрель","Май"],
#     "Summer": ["Июнь", "Июль", "Август"],
#     "Autumn": ["Сентябрь", "Октябрь", "Ноябрь"]
# }

# with open("analyzeslaries.txt", "r") as file:
#     for i in file:
#         month, salary = i.split()
#         if month in seasons["Winter"]:
#             list1[month] = int(salary)
#             print(salary)
# print(sum(list1.values()))



# Я хочу разделить на сезоны месяцы
# Открыть файл формата текст с данными
# Скопировать данные в лист1 с типом данных дикт
# сказать что зарплата в относится к сезонам
# вывести зп сезона



# 1. Чтение файла:
# Откройте файл "data.txt" в режиме чтения.
# Прочитайте все строки из файла и выведите их на экран.

# with open ("data.txt", "r") as file:
#     print(file.readlines())

# Закройте файл.
# 2. Запись в файл:
# Откройте файл "data.txt" в режиме записи.
# Запишите в файл строку "Привет, мир!".
# Закройте файл.

# file = open("data.txt", "w")
# file.write("Hello world")
# file.close()

# with open ("data.txt", "r") as file:
#     print(file.readlines())


# 3. Добавление в файл:
# Откройте файл "data.txt" в режиме дозаписи.
# Добавьте в файл строку "Это вторая строка.".
# Закройте файл.

# file = open("data.txt", "a")
# file.write("This is second str \n")
# file.close()

# with open("data.txt", "r") as file:
#     print(file.readlines())


# 4. Поиск в файле:
# Откройте файл "data.txt" в режиме чтения.
# Проверьте, есть ли в файле строка "привет".
# Если строка найдена, выведите сообщение "Строка найдена!".


# with open("data.txt", "r") as file:
#     for i in file:
#         if i == "Привет":
#             print("Str is found")
           
#         else:
#             print("str is not found")



# 5. Замена в файле:
# Откройте файл "data.txt" в режиме чтения.
# Прочитайте все строки из файла.
# Замените все вхождения слова "привет" на слово "здравствуйте".
# Закройте файл.

# file = open("data.txt", "r")
# lines = file.readlines()
# file.close()

# with open("data.txt", "w") as file:
#     for line in lines:
#         file.write(line.replace("привет", "здравствуйте"))

# Дата.ткст
# smad asdasdma
# sdma;dmas;
# Привет world
# Привет
# здравствуйте south
# здравствуйте 

#             Я не знаю почему так выходит: Количество слов в файле: 0
# 6. Подсчет слов в файле:
# Откройте файл "data.txt" в режиме чтения.
# Разделите текст на слова.
# Подсчитайте количество слов в файле.
# Выведите количество слов на экран.
# Закройте файл.


# with open("data.txt", "r") as f:
#     lines = f.readlines()
#     wordcount = 0
#     for i in lines:
#         words = i.split()
#         wordcount += len(words)
# print("Количество слов в файле:", wordcount)



# 7. Подсчет строк в файле:
# Откройте файл "data.txt" в режиме чтения.
# Прочитайте все строки из файла.
# Подсчитайте количество строк в файле.
# Выведите количество строк на экран.
# Закройте файл.


# with open("data.txt", "r") as f:
#     lines = f.readlines()
#     countl = len(lines)
# print(countl)



# 8. Сортировка строк в файле:
# Откройте файл "data.txt" в режиме чтения.
# Прочитайте все строки из файла.
# Сортируйте строки по алфавиту.
# Запишите отсортированные строки обратно в файл.
# Закройте файл.

# with open("data.txt", "r") as f:
#     lines = f.readlines()
#     lines.sort()
# with open("data2.txt", "w") as f:
#     for i in lines:
#         f.write(i)




# 9. Объединение двух файлов:
# Откройте два файла "data1.txt" и "data2.txt" в режиме чтения.
# Прочитайте все строки из обоих файлов.
# Объедините строки из двух файлов в один список.
# Запишите объединенный список в новый файл "data3.txt".
# Закройте все файлы.





# 10. Разделение файла на части:
# Откройте файл "data.txt" в режиме чтения.
# Разделите файл на части по 100 строк.
# Сохраните каждую часть в отдельный файл с именем "data_part1.txt", "data_part2.txt" и т.д.
# Закройте файл.
