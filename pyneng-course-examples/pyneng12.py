from re import T

def check_password(username, password, min_len=8, check_numbers = False):
    print(f"{username=} {password=} {min_len=}")
    if type(username) != str or type(password) != str:
        raise ValueError("надо передавать строки")
    if len(password) < min_len:
        print("Пароль слишком мал")
        return False
    elif username.lower() in password.lower():
        print("Пароль содержит имя пользователя")
        return False
    elif check_numbers and len(set("0123456789") & set(password)) < 3:
        print("В пароле должно быть хотя бы 3 уникальных числа")
        return False
    else:
        print(f"Пароль для пользователя {username} установлен")
        return True
    print("#"*40)
def check_user_list(user_passwd_data):
    wrong_users = []
    correct_users = []
    for user, passwd in user_passwd_data:
        print(user,passwd)
        try:
            check = check_password(user, passwd)
        except ValueError as error:
            print(error)
        if check:
            correct_users.append(user)
        else:
            wrong_users.append(user)
def main():
    data = [
        ["user1", "asddwafaew"],
        ["user2", 'asda'],
        ["user0", '01'],
        [10,12],
        ["user3", 'asdasdasdasd'],
    ]

    check_user_list(data)
    print(check_user_list)
    

main()