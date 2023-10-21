# ip = "192.168.20.2"
# octets = ip.split('.')
# octets_int = []
# for i in octets:
#    octets_int.append(i)

# for number in range(11):
#     print(f"interface Gi/{number}")

# # распаковка словаря
# for item in r1.items():
#     key, value = item
# for key, value in r1.items():
#     print(key,value)

# commands = [
#     "switchport mode access",
#     "switchport access vlan",
#     "spanning-tree portfast",
#     "spanning-tree bpduguard enable",
# ]
# access = {'0/12':10, '0/14':11, '0/16':17, '0/17': 150}

# for intf, vlan in access.items(): # перебор словаря акцес по значениям ключ - содержимое за счет метода items
#     print(f"interface {intf}")
#     for cmd in commands: # для коммандс по  кмд элементам в переменную
#         if cmd.endswith("vlan"): # если строка заканчивается на влан тогда
#             print(f"{cmd} {vlan}") # принтим 
#         else:
#             print(f"{cmd}")

