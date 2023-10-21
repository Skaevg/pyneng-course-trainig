username = input('Введите имя пользователя: ')
password = input('Введите пароль: ')


while True:
    if len(password) < 8:
        print("Пароль слишком короткий")
    elif username.lower() in password.lower():
        print("Пароль содержит имя пользователя")
    elif len(set("0123456789") & set(password)) < 3 :
        print("В пароле ддолжно быть мин 3 уникальных цифры")
    else:
        print(f"Пароль для {username} прошел все проверки")
        break
    password = input("Введите пароль ешё раз: ")


# while not password_correct:
#     if len(password) < 8:
#         print("Пароль слишком короткий")
#         password = input("Введите пароль ешё раз: ")
#     elif username.lower() in password.lower():
#         print("Пароль содержит имя пользователя")
#         password = input("Введите пароль ешё раз: ")
#     elif len(set("0123456789") & set(password)) < 3 :
#         print("В пароле ддолжно быть мин 3 уникальных цифры")
#         password = input("Введите пароль ешё раз: ")
#     else:
#         print(f"Пароль для {username} прошел все проверки")
#         password_correct = True

# print("#"*40)

