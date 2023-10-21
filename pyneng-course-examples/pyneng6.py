

# input_1 = input("Введите число: ")

# if input_1.strip().isdigit(): # проверка на число
#     num1 = int(input_1)
#     print(num1 * 100)
# else:
#     print("Надо ввести число")

# print("="*40)

# try:
#     num1 = int(input_1)
#     print(num1/0)
# except ValueError: #перехват исключения
#     print("надо вводить только числа")
# except ZeroDivisionError:
#     print("Не делиться на ноль")
# print("="*40)

ip_list = ["10.1.1.1", "10.2.2.2","10.3.3.3"]
for ip in ip_list:
    print(f"Подключение на {ip}")
    try:
        if ip == "10.1.1.1":
            int(ip)
    except ValueError:
        print(f"На оборудовании {ip} что-то пошло не так")
    print(f"{ip} отработало")
    # finally: # когда надо чтобы делал в любом случае
    #     print("закрытие файла")