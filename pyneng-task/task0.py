# Задание 5.1
# В задании создан словарь, с информацией о разных устройствах.
# Необходимо запросить у пользователя ввод имени устройства (r1, r2 или sw1). И вывести информацию о соответствующем устройстве на стандартный поток вывода (информация будет в виде словаря).
# Пример выполнения скрипта:
# $ python task_5_1.py
# Введите имя устройства: r1
# {'location': '21 New Globe Walk', 'vendor': 'Cisco', 'model': '4451', 'ios': '15.4', 'ip': '10.255.0.1'}
# Ограничение: нельзя изменять словарь london_co.
# Все задания надо выполнять используя только пройденные темы. То есть эту задачу можно решить без использования условия if.
# name_devices = input("Введите имя устройства: ")
# london_co = {
#     "r1": {
#         "location": "21 New Globe Walk",
#         "vendor": "Cisco",
#         "model": "4451",
#         "ios": "15.4",
#         "ip": "10.255.0.1"
#     },
#     "r2": {
#         "location": "21 New Globe Walk",
#         "vendor": "Cisco",
#         "model": "4451",
#         "ios": "15.4",
#         "ip": "10.255.0.2"
#     },
#     "sw1": {
#         "location": "21 New Globe Walk",
#         "vendor": "Cisco",
#         "model": "3850",
#         "ios": "3.6.XE",
#         "ip": "10.255.0.101",
#         "vlans": "10,20,30",
#         "routing": True
#     }
# }
# print(london_co[name_devices])

# Задание 5.1a
# Переделать скрипт из задания 5.1 таким образом, чтобы, кроме имени устройства, запрашивался также параметр устройства, который нужно отобразить.
# Вывести информацию о соответствующем параметре, указанного устройства.

# name_devices = input("Введите имя устройства: ").lower()

# london_co = {
#     "r1": {
#         "location": "21 New Globe Walk",
#         "vendor": "Cisco",
#         "model": "4451",
#         "ios": "15.4",
#         "ip": "10.255.0.1"
#     },
#     "r2": {
#         "location": "21 New Globe Walk",
#         "vendor": "Cisco",
#         "model": "4451",
#         "ios": "15.4",
#         "ip": "10.255.0.2"
#     },
#     "sw1": {
#         "location": "21 New Globe Walk",
#         "vendor": "Cisco",
#         "model": "3850",
#         "ios": "3.6.XE",
#         "ip": "10.255.0.101",
#         "vlans": "10,20,30",
#         "routing": True
#     }
# }
# param_devices = input(f"Введите имя параметра:{set(london_co[name_devices].keys())}").lower()

# if param_devices in london_co[name_devices]:
#     print(london_co[name_devices][param_devices])
# else:
#     print('Такого параметра нет')

# Network:
# 10        1         1         0
# 00001010  00000001  00000001  00000000

# Mask:
# /24
# 255       255       255       0
# 11111111  11111111  11111111  00000000

# ip = input("введите ip: ").split(".")
# ip0 = ip[-1].split("/")
# ip.pop()
# ip.append(ip0[0])
# ip.append(ip0[-1])
# integer_numbers = [int(x) for x in ip]
# ip1, ip2, ip3, ip4, gt= integer_numbers
# gt1, gt2, gt3, gt4 = 255, 255, 255, 0
# print("Network:")
# print("{:<15} {:<15} {:<15} {:<15}".format(ip1,ip2,ip3,ip4))
# print("{:<15b} {:<15b} {:<15b} {:<15b}".format(ip1,ip2,ip3,ip4))
# print()
# print("Mask:")
# print(f"/{gt}")
# print("{:<15} {:<15} {:<15} {:<15}".format(gt1,gt2,gt3,gt4))
# print("{:<15b} {:<15b} {:<15b} {:<15b}".format(gt1,gt2,gt3,gt4))

# interface_type_work = input('Введите режим работы интерфейса (access/trunk): ')
# interface_number = input("Введите тип и номер интерфейса: ")

# access_template = [
#     "switchport mode access", 
#     "switchport access vlan {}",
#     "switchport nonegotiate", 
#     "spanning-tree portfast",
#     "spanning-tree bpduguard enable"
# ]

# trunk_template = [
#     "switchport trunk encapsulation dot1q", 
#     "switchport mode trunk",
#     "switchport trunk allowed vlan {}"
# ]
 
# if interface_type_work == "trunk":
#     vlan_trunk = input("Введите разрешенные VLANы: ")
#     print("interface " + interface_number)
#     for data in trunk_template:
#         if data.endswith("{}"):
#             print(data.replace("{}", vlan_trunk))
#         else:
#             print(data)
# elif interface_type_work == "access":
#     vlan_access = input("Введите номер VLAN: ")
#     print("interface " + interface_number)
#     for data in access_template:
#         if data.endswith("{}"):
#             print(data.replace("{}", vlan_access))
#         else:
#             print(data)