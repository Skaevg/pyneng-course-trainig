# Создать функцию generate_trunk_config, которая генерирует конфигурацию для trunk-портов.
# У функции должны быть такие параметры:
#     intf_vlan_mapping: ожидает как аргумент словарь с соответствием интерфейс-VLANы такого вида:

# {"FastEthernet0/1": [10, 20],
#  "FastEthernet0/2": [11, 30],
#  "FastEthernet0/4": [17]}

#     trunk_template: ожидает как аргумент шаблон конфигурации trunk-портов в виде списка команд (список trunk_mode_template)
# Функция должна возвращать список команд с конфигурацией на основе указанных портов и шаблона trunk_mode_template. В конце строк в списке не должно быть символа перевода строки.
# Проверить работу функции на примере словаря trunk_config и списка команд trunk_mode_template. Если эта проверка прошла успешно, проверить работу функции еще раз на словаре trunk_config_2 и убедится, что в итоговом списке правильные номера интерфейсов и вланов.
# Пример итогового списка (перевод строки после каждого элемента сделан для удобства чтения):

# [
# "interface FastEthernet0/1",
# "switchport mode trunk",
# "switchport trunk native vlan 999",
# "switchport trunk allowed vlan 10,20,30",
# "interface FastEthernet0/2",
# "switchport mode trunk",
# "switchport trunk native vlan 999",
# "switchport trunk allowed vlan 11,30",
# ...]

# Ограничение: Все задания надо выполнять используя только пройденные темы.


def generate_trunk_config(intf_vlan_mapping, trunk_template):
    for intf,vlan in intf_vlan_mapping.items():
        print(f"{intf}")
        for template in trunk_template:
            if template.endswith("vlan"):
                vlans = str(vlan)
                print(f"{template} {vlans}")
            else: print(template)


trunk_mode_template = [
    "switchport mode trunk", "switchport trunk native vlan 999",
    "switchport trunk allowed vlan"
]

trunk_config = {
    "FastEthernet0/1": [10, 20, 30],
    "FastEthernet0/2": [11, 30],
    "FastEthernet0/4": [17]
}

generate_trunk_config(trunk_config, trunk_mode_template)

# trunk_filter = {}
# for key, value in trunk_config.items():
#     print(key)
#     print(value)

# key = [(key, value) for key, value in trunk_config.items()]
# print(key)

# intf = [key for key, value in r1.items()]
# vlans = [value for key, value in r1.items()]


# def generate_access_config(access_config, access_mode_template, psecurity=None):
#     for intf,vlan in access_config.items():
#         print(f"{intf}")
#         for template in access_mode_template:
#             if template.endswith("vlan"):
#                 print(f"{template} {vlan}")
#             else: print(template)
#     if psecurity != None:
#         for security in psecurity:
#             print(security)
    