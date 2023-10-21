# Задание 9.1
# Создать функцию, которая генерирует конфигурацию для access-портов.
# Функция ожидает такие аргументы:
# словарь с соответствием интерфейс-VLAN такого вида:

# {"FastEthernet0/12": 10,
#  "FastEthernet0/14": 11,
#  "FastEthernet0/16": 17}

# шаблон конфигурации access-портов в виде списка команд (список access_mode_template)
# Функция должна возвращать список всех портов в режиме access с конфигурацией на основе шаблона access_mode_template. В конце строк в списке не должно быть символа перевода строки.
# В этом задании заготовка для функции уже сделана и надо только продолжить писать само тело функции.
# Пример итогового списка (перевод строки после каждого элемента сделан для удобства чтения):

# [
# "interface FastEthernet0/12",
# "switchport mode access",
# "switchport access vlan 10",
# "switchport nonegotiate",
# "spanning-tree portfast",
# "spanning-tree bpduguard enable",
# "interface FastEthernet0/17",
# "switchport mode access",
# "switchport access vlan 150",
# "switchport nonegotiate",
# "spanning-tree portfast",
# "spanning-tree bpduguard enable",
# ...]

# Проверить работу функции на примере словаря access_config и списка команд access_mode_template. Если предыдущая проверка прошла успешно, проверить работу функции еще раз на словаре access_config_2 и убедиться, что в итоговом списке правильные номера интерфейсов и вланов.
# Ограничение: Все задания надо выполнять используя только пройденные темы.
# def generate_access_config(intf, vlan):
#     print(f"{intf}")
#     for template in access_mode_template:
#         if template.endswith("vlan"):
#             print(f"{template} {vlan}")
#         else: print(template)

# access_mode_template = [
#     "switchport mode access", "switchport access vlan",
#     "switchport nonegotiate", "spanning-tree portfast",
#     "spanning-tree bpduguard enable"
# ]

# # access_config = {
# #     "FastEthernet0/12": 10,
# #     "FastEthernet0/14": 11,
# #     "FastEthernet0/16": 17
# # }
# access_config = {
#     "FastEthernet0": "10"
# }

# access_config_2 = {
#     "FastEthernet0/03": 100,
#     "FastEthernet0/07": 101,
#     "FastEthernet0/09": 107,
# }

# for intf,vlan in access_config_2.items():
#     generate_access_config(intf,vlan)

# 9.1a
# Дополнить скрипт: ввести дополнительный параметр, который контролирует будет ли настроен port-security:
#     имя параметра «psecurity» по умолчанию значение None
#     для настройки port-security, как значение надо передать список команд port-security (находятся в списке port_security_template)
# Функция должна возвращать список всех портов в режиме access с конфигурацией на основе шаблона access_mode_template и шаблона port_security_template, если он был передан. В конце строк в списке не должно быть символа перевода строки.
# Проверить работу функции на примере словаря access_config, с генерацией конфигурации port-security и без.



def generate_access_config(access_config, access_mode_template, psecurity=None):
    for intf,vlan in access_config.items():
        print(f"{intf}")
        for template in access_mode_template:
            if template.endswith("vlan"):
                print(f"{template} {vlan}")
            else: print(template)
    if psecurity != None:
        for security in psecurity:
            print(security)
    

access_mode_template = [
    "switchport mode access", "switchport access vlan",
    "switchport nonegotiate", "spanning-tree portfast",
    "spanning-tree bpduguard enable"
]

port_security_template = [
    "switchport port-security maximum 2",
    "switchport port-security violation restrict",
    "switchport port-security"
]

access_config = {"FastEthernet0/12": 10, "FastEthernet0/14": 11, "FastEthernet0/16": 17}


generate_access_config(access_config, access_mode_template)
generate_access_config(access_config, access_mode_template, port_security_template)