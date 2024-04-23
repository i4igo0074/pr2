# a = [12, 4 ,5, 7, 9]
# sum = 0
# i = 0
# while i < len(a):
#     if a[i] == 7:
#         break
#     print(i, a[i])
#     sum += a[i]
#     i += 1
# print(sum)


# sumi = 0
# i = 0
# while i < 100:
#     if str(i) == str(i)[::-1]:
#         print(i)
#         sumi += i
#     i += 1
# print(sumi)


# while True:
#     print("Hello")
# c = 0
# i = 0
# while i < len(a):
#     print(i, a[i])
#     c += a[i]
#     i += 1
# print(c)

# a = [12, 4, 5, 4, 6, 7, 8]

# c = 0
# i = 0
# while i < len(a):
#     if a[i] == 6:
#         i += 1
#         continue
#     print(i, a[i])
#     c += a[i]
#     i += 1
# print(c)


# new_list = []
# while True:
#     input_text = input('Enter number: ')
#     if input_text == 'stop':
#         break
#     new_list.append(input_text)
#     print(new_list)

# new_list = []
# while True: 
#     print('1. Добавить число\n2. Посмотреть лист')
#     action = input('Enter action: ')
#     if action == '1':
#         num = input('Enter number: ')
#         new_list.append(num)
#         print(f'Успешно добавили цифру {num}')
#     elif action == '2':
#         print(new_list)
#     print()
#     print()



# while True:
    
#     print("Enter 1 to *: \n2. Enter 2 to /: \n3.Enter 3 to +: \n.4. Enter 4 to -: ")


#     action = int(input("Enter num of action: "))
#     if action == 1:
#         num1 = int(input("Enter 1st num: "))
#         num2 =  int(input("Enter 2nd num: "))
#         sum1 = num1 * num2
#         print(f"{num1}*{num2} = {sum1}")
        
#     elif action == 2:
#         num1 = int(input("Enter 1st num: "))
#         num2 =  int(input("Enter 2nd num: "))
#         sum1 = num1 / num2
#         print(f"{num1}/{num2} = {sum1}")
        
#     elif action == 3:
#         num1 = int(input("Enter 1st num: "))
#         num2 =  int(input("Enter 2nd num: "))
#         sum1 = num1 + num2
#         print(f"{num1}+{num2} = {sum1}")
        
#     elif action == 4:
#         num1 = int(input("Enter 1st num: "))
#         num2 =  int(input("Enter 2nd num: "))
#         sum1 = num1 - num2
#         print(f"{num1}-{num2} = {sum1}")
        
# while True:
#     num1 = int(input("Enter 1st num: "))
#     num2 =  int(input("Enter 2nd num: "))
#     print("Enter 1 to *: \n2. Enter 2 to /: \n3.Enter 3 to +: \n.4. Enter 4 to -: ")
#     action = int(input("Enter num of action: "))
#     if action == 1:
#         sum1 = num1 * num2
#         print(f"{num1}*{num2} = {sum1}")
#     elif action == 2:
        
#         if num2 == 0:
#             print("Error")
#             continue
#         sum1 = num1 / num2
#         print(f"{num1}/{num2} = {sum1}")
#     elif action == 3:
#         sum1 = num1 + num2
#         print(f"{num1}+{num2} = {sum1}")
#     elif action == 4:
#         sum1 = num1 - num2
#         print(f"{num1}-{num2} = {sum1}")


# import requests
# token = "7064989440:AAFKmZg4n6jWuGd8WfSPTaSniQwdHQ6lnNU"
# url = f'https://api.telegram.org/bot{token}/sendMessage'
# params = {
#     "chat_id": "84602916",
#     "text": "Hello"
# }
# while True:
    
#     requests.post(url, params)


# import requests
# users = {
#     1166930953: "Bektur",
#     84602916: "Isa",
#     260094427: "Alan"}
# token = "7064989440:AAFKmZg4n6jWuGd8WfSPTaSniQwdHQ6lnNU"
# url = f'https://api.telegram.org/bot{token}/sendMessage'

# for i in users:
#         params = {
#             "chat_id": i,
#             "text": "Hi " + users[i],
#         }
#         r = requests.post(url, params)
#         print(r)

