# Создать функцию get_int_vlan_map, которая обрабатывает конфигурационный файл коммутатора и возвращает кортеж из двух словарей:
#     словарь портов в режиме access, где ключи номера портов, а значения access VLAN (числа):

# {"FastEthernet0/12": 10,
#  "FastEthernet0/14": 11,
#  "FastEthernet0/16": 17}

#     словарь портов в режиме trunk, где ключи номера портов, а значения список разрешенных VLAN (список чисел):

# {"FastEthernet0/1": [10, 20],
#  "FastEthernet0/2": [11, 30],
#  "FastEthernet0/4": [17]}

# У функции должен быть один параметр config_filename, который ожидает как аргумент имя конфигурационного файла.
# Проверить работу функции на примере файла config_sw1.txt
# Ограничение: Все задания надо выполнять используя только пройденные темы.


from csv import list_dialects


def get_int_vlan_map(config_filename):
    pass

# with open("config_sw2.txt") as f:
#     key = []
#     config_file = f.read()
#     config_file2 = config_file.replace("!","")
#     config = config_file2.split("\n")
#     print(config)
#     # for line in config:
#     #     print(line)
#     #     if line.startswith("interface"):
#     #         if line[10:].startswith("Vlan"):
#     #             pass_line = line 
#     #         else: 
#     #             key.append(line[10:])
#     # print(key)

with open("config_sw1.txt") as f:
    key = []
    key_access = []
    key_trunk = []
    key_a = []
    value_a = []
    dict_a = {}
    key_t = []
    value_t = []
    dict_t = {}
    config_file = f.read()
    config_file2 = config_file.replace("\n","")
    config = config_file2.split("!")
    for line in config:
        if line.startswith("interface") and not line[10:].startswith("Vlan"):
            key = line
            if key.find("access") > 1:
                key_access.append(key)
            elif key.find("trunk") > 1:
                key_trunk.append(key)
    for i_ac in key_access:
        key_access_sp = i_ac.split()
        for access_split in key_access_sp:
            if access_split.find("ast") >= 1:
                key_a.append(access_split)
            elif access_split.isdigit():
                value_a.append(access_split)
        dict_a = dict(zip(key_a, value_a))

    for i_ac in key_trunk:
        key_trunk_sp = i_ac.split()
        for trunk_split in key_trunk_sp:
            vlans_trunk = str(trunk_split.split(','))
            if vlans_trunk.find("ast") >= 1:
                key_t.append(trunk_split)
            elif vlans_trunk[2].isdigit():
                value_t.append(trunk_split)
        dict_t = dict(zip(key_t, value_t))
    print(dict_a)
    print(dict_t)
