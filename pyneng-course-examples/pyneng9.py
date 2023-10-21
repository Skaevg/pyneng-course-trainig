# from glob import glob
# path = "/home/vargrant/repos/pyneng-11" #путь к файлам
# # fl = "~/repos/template/data.txt"
# files = ["sh_cdp_n_r1.txt","sh_cdp_n_r2.txt","sh_cdp_n_r3.txt","sh_cdp_n_sw1.txt",]
# files = glob["sh_cdp_n_*.txt"] # глоб дает выбор файлов (в виде строки) * - значит все  варианты без ограничений.
# for file in files:
#     with open(f"{path}{file}", "r") as f:
#         for line in f:
#             if "Eth" in line:
#                 print(line.rstrip())
    

result = [
    ["FastEthernet0/0", "15.0.15.1"],
    ["FastEthernet0/0", "15.0.15.1"],
    ["FastEthernet0/0", "15.0.15.1"],
]

result_list = []

# with open("sh_ip_int_br.txt", 'r') as f:
#     for line in f: # перебираем строки
#         line_list = line.split() # разбиваем
#         if line_list: #if len(line_list != 0) # если пришла не пустой
#             str_index_0 = line_list[0] 
#             if str_index_0[-1].isdigit(): # если последний символ цифра
#                 intf_ip_list = line_list[:2] # записываем срез списка.
# print(result_list)

# with open("sh_ip_int_br.txt", 'r') as f:
#     for line in f:
#         line_list = line.split()
#         if line_list and line_list[0][-1].isdigit(): # если список не пустой, проверка на последний символ по цифре.
#             intf_ip_list = line_list[:2] # в переменную закидываем срез 
#             result_list.append(intf_ip_list) # добавляем в словарь.
        
# print(result_list)

result_dict = []

with open("sh_ip_int_br.txt", 'r') as f:
    for line in f:
        line_list = line.split()
        if line_list and line_list[0][-1].isdigit(): # если список не пустой, проверка на последний символ по цифре.
            intf, ip = line_list[:2] # в переменную закидываем срез 
            intf = line_list[0]
            ip = line_list[1]
            if ip  == "unassigned":
                ip = None
                result_dict[intf] = ip
print(result_dict)
for intf, ip in result_dict.items():
    if ip:
        print(intf)
        
