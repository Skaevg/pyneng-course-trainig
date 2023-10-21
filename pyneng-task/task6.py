# Создать функцию convert_config_to_dict, которая обрабатывает конфигурационный файл коммутатора и возвращает словарь:
#     Все команды верхнего уровня (глобального режима конфигурации), будут ключами.
#     Если у команды верхнего уровня есть подкоманды, они должны быть в значении у соответствующего ключа, в виде списка (пробелы в начале строки надо удалить).
#     Если у команды верхнего уровня нет подкоманд, то значение будет пустым списком
# У функции должен быть один параметр config_filename, который ожидает как аргумент имя конфигурационного файла.
# При обработке конфигурационного файла, надо игнорировать строки, которые начинаются с «!», а также строки в которых содержатся слова из списка ignore. Для проверки надо ли игнорировать строку, использовать функцию ignore_command.
# Проверить работу функции на примере файла config_sw1.txt
# Часть словаря, который должна возвращать функция (полный вывод можно посмотреть в тесте test_task_9_4.py):

# {
#     "version 15.0": [],
#     "service timestamps debug datetime msec": [],
#     "service timestamps log datetime msec": [],
#     "no service password-encryption": [],
#     "hostname sw1": [],
#     "interface FastEthernet0/0": [
#         "switchport mode access",
#         "switchport access vlan 10",
#     ],
#     "interface FastEthernet0/1": [
#         "switchport trunk encapsulation dot1q",
#         "switchport trunk allowed vlan 100,200",
#         "switchport mode trunk",
#     ],
#     "interface FastEthernet0/2": [
#         "switchport mode access",
#         "switchport access vlan 20",
#     ],
# }

# Ограничение: Все задания надо выполнять используя только пройденные темы.



# def ignore_command(command, ignore):
#     """
#     Функция проверяет содержится ли в команде слово из списка ignore.

#     command - строка. Команда, которую надо проверить
#     ignore - список. Список слов

#     Возвращает
#     * True, если в команде содержится слово из списка ignore
#     * False - если нет
#     """
#     ignore_status = False
#     for word in ignore:
#         if word in command:
#             ignore_status = True
#     return ignore_status

# # with open(file) as f:
# #     conf_file = f.read()
# #     print(conf_file)
# def convert_config_to_dict(file):
#     value_t = []
#     true_conf= []
#     with open(file, 'r') as f:
#         conf_file = f.read()
#         conf_split = conf_file.split("\n")
#         for f in conf_split:
#             if ignore_command(f, ignore) == False:
#                 true_conf.append(f)
#                 for i in true_conf:
#                     print(i)
#                     key_t = dict(zip(i,value_t))
#                     if not i.startswith(" "):
#                         dict_t = dict(zip(i, value_t))
#                     else: dict_t = dict(zip(key_t,i)) 
#                     # print(dict_t)
#         # print(true_conf)



# ignore = ["duplex", "alias", "Current configuration", "!"]
# convert_config_to_dict(file="config_sw1.txt")



    # for i_ac in key_trunk:
    #     key_trunk_sp = i_ac.split()
    #     for trunk_split in key_trunk_sp:
    #         vlans_trunk = str(trunk_split.split(','))
    #         if vlans_trunk.find("ast") >= 1:
    #             key_t.append(trunk_split)
    #         elif vlans_trunk[2].isdigit():
    #             value_t.append(trunk_split)
    #     dict_t = dict(zip(key_t, value_t))

# -*- coding: utf-8 -*-



def ignore_command(command, ignore_list):
    for word in ignore_list:
        if word in command:
            return True
    return False


def convert_config_to_dict(config_filename, ignore_lines):
    config_dict = {}
    with open(config_filename) as f:
        for line in f:
            line = line.rstrip()
            if line and not (
                line.startswith("!") or ignore_command(line, ignore_lines)
            ):
                if line[0].isalnum():
                    section = line
                    config_dict[section] = []
                else:
                    config_dict[section].append(line.strip())
    return config_dict

ignore = ["duplex", "alias", "Current configuration"]
ignore_command(file="config_sw1.txt", ignore)
convert_config_to_dict(file="config_sw1.txt",)

