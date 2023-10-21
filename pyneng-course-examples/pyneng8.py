f = open ('file_name.txt', 'r')
# print(f.read())
# print(f.readlines())
# f.seek(0)
# f.readlines()
# print(f.readlines())
# for line in f: # перебирает по одной строке, не загружает в память. в отличии от ридлайнс.
#     print(line.rstrip())
# while True:
#     line = print(f.readline())
#     if not line: # когда строка пустая брейк
#         break

f_out = open("result.txt", 'w')
f_out.write('line1')


with open("result3.txt", 'w') as f:
    f.writelines(lines)
    # raise ValueError

print("#"*50) 

with open("sh_ip_int_br.txt", "r") as f:
    for line in f:
        print(line.rstrip())

with open("sh_ip_int_br.txt","r") as f_read, open("result.txt", 'w') as f_write: # открыть файл и записать только строки начинающиеся с ФастЭзернет.
    for line in f_read:
        if line.startswith("FastEthernet"):
            f_write.write(line)
