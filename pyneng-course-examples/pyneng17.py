# print(list(zip([1,2,3], [10,20,30])))

# vlans = [10,20,30,40]
# vlans_name = ["IT","Management","Video","Sales"]

# for i in range(len(vlans)):
#     print(f"vlan {vlan[i]}")
#     print(f" name {vlans_name[i]}")

# print(zip(vlans, vlans_name))

# for vl, name in list(zip(vlans, vlans_name)):
#     print(f"vlan {vl}")
#     print(f" name {name}")

# from curses.ascii import isdigit


# data = [['FastEthernet0/0','15.15.1','up','up'],
#         ['FastEthernet0/1','15.16.1','up','up'],
#         ['FastEthernet0/2','15.17.1','up','up'],
#         ['FastEthernet0/3','15.18.1','up','up'],
#         ['FastEthernet0/4','15.19.1','up','up'],
#         ['FastEthernet0/5','15.10.1','up','up'],]
        
# headers = ['interface', 'ip', 'status', 'protocol']
# result = []
# for d_list in data:
#     item_dict = dict(zip(headers, d_list))
#     print(item_dict)

# for d_list in data:
#     item_dict = dict(zip(headers, d_list))
#     print(item_dict)
#     result.append(item_dict)

# print(result)

# for d in result: #вывод данных ип из словаря по ключу ип.
#     print(d["ip"])

# # генератор словареей
# print([dict(zip(headers, d_list)) for d_list in data])


# vlans = [10, 20, 30, 40]
# map(str, vlans) # фукнция мап берет каждый элемент  и применяет к нему функцию(стр) без скобок 

# print(list(map(str, vlans)))
# print([str(vl) for vl in vlans])

# [f"vlan {vl}" for vl in vlans]
# # вывод ['vlan 10', 'vlan 20', 'vlan 30', 'vlan 40']

# list(map(lambda vl: f"vlan {vl}", vlans))
# #аноним функция lambda vl(аргумент) после двоеточия что функция возвращает.


# vlansi = ["20", "14", "2", "as", "sw"]

# print([int(vl) for vl in vlansi if vl.isdigit()])
# print(list(filter(str.isdigit, vlansi)))
# print(list(map(int, filter(str.isdigit, vlansi))))

# all & any
# all тру если все тру, если одно значение фолс то все фолс.
# ip = "10.1.2.2"
# print([octet.isdigit() for octet in ip.split(".")])

# print(False in [octet.isdigit() for octet in ip.split(".")])
# print(False not in [octet.isdigit() for octet in ip.split(".")])
# print(all([octet.isdigit() for octet in ip.split(".")]))

# any если один из множества тру выполняй.
# ignore = ['duplex', 'alias', 'currect configuration']

# with open("config_sw1.txt") as f:
#     for line in f:
#         if any([word in line for word in ignore]): # если что-то из этого возвращает ТРУ игнорирует строку, иначе принт 
#             pass
#         else:
#             print(line.rstrip())

ignore = ['duplex', 'alias', 'currect configuration']

with open("config_sw1.txt") as f:
    for line in f:
        if not any([word in line for word in ignore]): # если что-то из этого возвращает ТРУ игнорирует строку, иначе принт 
            print(line.rstrip())
            