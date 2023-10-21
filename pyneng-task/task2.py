# Задание 7.1
# Обработать строки из файла ospf.txt и вывести информацию по каждой строке в таком виде на стандартный поток вывода:

# Prefix                10.0.24.0/24
# AD/Metric             110/41
# Next-Hop              10.0.13.3
# Last update           3d18h
# Outbound Interface    FastEthernet0/0

# Ограничение: Все задания надо выполнять используя только пройденные темы.

# columns = ["Prefix", "AD/Metric", "Next-Hop", "Last update", "Outbound Interface"]

# with open("ospf.txt") as f:
#     line_ospf = f.read()
# section = line_ospf.split("O        ")
# resection = section[1:]
# for sec in resection:
#     result = sec.split()
#     print(f"{columns[0]} {result[0]}\n",
#           f"{columns[1]} {result[1]}\n",
#           f"{columns[2]} {result[3]}\n",
#           f"{columns[3]} {result[4]}\n",
#           f"{columns[4]} {result[5]}\n",)

# Задание 7.2

# Создать скрипт, который будет обрабатывать конфигурационный файл config_sw1.txt. Имя файла передается как аргумент скрипту.
# Скрипт должен возвращать на стандартный поток вывода команды из переданного конфигурационного файла, исключая строки, которые начинаются с !.
# Вывод должен быть без пустых строк.
# Ограничение: Все задания надо выполнять используя только пройденные темы.
# Пример вывода:

# $ python task_7_2.py config_sw1.txt
# Current configuration : 2033 bytes
# version 15.0
# service timestamps debug datetime msec
# service timestamps log datetime msec
# no service password-encryption
# hostname sw1
# interface Ethernet0/0
#  duplex auto
# interface Ethernet0/1
#  switchport trunk encapsulation dot1q
#  switchport trunk allowed vlan 100
#  switchport mode trunk
#  duplex auto
#  spanning-tree portfast edge trunk
# interface Ethernet0/2
#  duplex auto
# interface Ethernet0/3
#  switchport trunk encapsulation dot1q
#  switchport trunk allowed vlan 100
#  duplex auto
#  switchport mode trunk
#  spanning-tree portfast edge trunk
# ...

# with open("config_sw1.txt") as f:
#     lines_config = f.read()
# # print(lines_config)
# splt_config = lines_config.split("!\n")
# # print(splt_config)
# for i in splt_config:
#     if i.startswith("")
