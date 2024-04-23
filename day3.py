text = "kazakhsatan is country. great britain is the city"

# print(text.upper()) заглавные
# print(text.lower()) from small letters
# print(text.title()) fromt title every word
# print(text.capitalize()) make title first letter
# print(text.swapcase()) totally change/swap registr of letters

# print(text.replace("country", "city")) exchange string

# print(text.split()) #separete each word to list, u can split with ("."), ('a') 

# print(len(text)) length of str
print(len(text.split('.'))) #length of list
# print(text.count("HI")) #count of HI
# print(text.find("Hi")) #index of HI, if there is no word HI in text, it returns -1, in other cases it will show number of index
# print(text[3])
# print(text.find("o"))

# text = "1234"
# print(text.isdigit()) #is text digit? it check
# print(text.isalpha()) #is text contains from alphabet?

# age = input("Enter your age: ")
# if age.isdigit():
#     print("Your age is", age)
# else:
#     print("Enter digit")    


# name = input("Enter your name as Mr.Muscle or Mrs.Sunda or Ms.Alan: ")
# if name.startswith("Mr."):
#     print("Hello sir")
# elif name.startswith("Mrs."):
#     print("Hello madam")
# else:
#     print("Hello")


"""
1. Напишите код, который запрашивает у пользователя имя, возраст и город. Выведите эти данные на экран в виде приветствия.
Преобразуйте строку в верхний регистр, нижний регистр, заглавные буквы в каждом слове и заглавную первую букву.
Разбейте строку на список по пробелу и по точке.
Найдите длину строки, количество вхождений подстроки и индекс первого вхождения.
Напишите код, который заменяет все символы "a" в строке на "o"."""

# name = input("Write your name: ")
# age = int(input("Write your age: "))
# city = input("Write your city: ")
# print("Hi", name, "whom", age, "from", city)

# text = "the cat chased the mouse quickly"
# print(text.upper())
# print(text.lower())
# print(text.title()) 
# print(text.capitalize())
# print(len(text)) 
# print(text.count("cat"))
# print(text.find("cat"))



# print(text.replace("a", "o"))

# Проверка наличия символов:
# Пользователь вводит строку. Проверьте, содержит ли она символ '@'. Если да, выведите сообщение "В строке есть символ @".
#field = input("Enter text: ")
# if "@" in field:
#     print("There is symbol @")
# else:
#     print("No such symbol") 

# Проверка наличия подстроки:
# Пользователь вводит строку. Проверьте, содержит ли она подстроку "Python". Если да, выведите сообщение "Строка содержит 'Python'".

# field = input("Enter text: ")
# if "Python" in field:
#     print("There is word Python")
# else:
#     print("No such Python") 

# Проверка на соответствие формату:
# Пользователь вводит email. Проверьте, является ли введенная строка действительным email адресом (содержит символ '@' и '.' после '@'). Выведите соответствующее сообщение.

# mail = input("Enter email: ")
# if "@" in mail and "." in mail :
#     print("Cool, this is your email:", mail)
# else:
#     print("Print correct with @.") 

# Поиск ключевых слов:
# Пользователь вводит текст. Проверьте, содержит ли введенный текст слово "спам" или "реклама". Если да, выведите сообщение "Текст содержит спам или рекламу".

# text = input("Enter message: ")
# if "spam" in text or "ad" in text or "advertisement" in text:
#     print("There are spam or ads in your text")
# else:
#     print("Your message were publicated")

# Проверка на число:
# Пользователь вводит строку. Проверьте, является ли она числом. Если да, выведите сообщение "Это число".

# enterdigit = input("Enter numbers: ")
# if enterdigit.isdigit():
#     enterdigit = int(enterdigit)
#     print("Cool, u entered nums")
# else:
#     print("Enter nums, not text")


# Проверка на длину строки:
# Пользователь вводит строку. Проверьте, состоит ли она из более чем 10 символов. Если да, выведите сообщение "Длина строки более 10 символов".

# string = input("Enter string pls: ")
# if len(string) >= 10:
#     print("Lenth of string consists more than 10 symbols")
# else:
#     print("Smthng goes wrong")




# Проверка на префикс:
# Пользователь вводит URL. Проверьте, начинается ли введенная строка с "http://". Если да, выведите сообщение "Это URL".

# urladress = input("Enter the name of URL: ")
# if urladress.startswith("http://"):
#     print("It is URL")
# else:
#     print("It is not URL")




# Проверка на наличие пробелов:
# Пользователь вводит строку. Проверьте, содержит ли она пробелы. Если да, выведите сообщение "Строка содержит пробелы".


# checkprobels = input("Enter text: ")
# if " " in checkprobels:
#     print("There are spaces")
# else:
#     print("Evrthng Ok")

# Проверка на верхний регистр:
# Пользователь вводит строку. Проверьте, все ли символы в строке находятся в верхнем регистре. Если да, выведите сообщение "Строка в верхнем регистре".

# checkreg = input("Enter text: ")
# if checkreg == checkreg.upper():
#     print("Str is in upper Reg.")
# else:
#     print("error")

