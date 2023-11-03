import subprocess

result = subprocess.run("ls")
print(result)
# result.returncode
# result = subprocess.run("ls -ls ipaddress".split()) # строка из команд, деляться по пробелу и превращаются в список
# result = subprocess.run(['ls', '-ls', 'ipaddress/*.py'], shell=True) # запустить шел для обработки *  как поиск всех елементов
# result = subprocess.run(['ping', '-c', '3', '-n', '8.8.8.8']) 
# result = subprocess.run(['ping', '-c', '3', '-n', '8.8.8.8'],) #  'returncode=1' 0 == норм, 1 == отказ

ip_list = ["8.8.8.8", "10.1.1.1", "8.8.4.4", 'test']
for ip in ip_list:
    result = subprocess.run(['ping', '-c', '3', '-n', ip], 
                            stdout=subprocess.PIPE, # перехват вывода. Значение DEVNULL вместо PIPE Это выбросить полученный текст
                            stderr=subprocess.PIPE, # перехват ошибок вывода. 
                            encoding="utf-8" # чтобы вывод кодировался, иначе байты выводит, можно узнать по знаку b' вначале
                            )
    if result.returncode == 0:
        print (f'Адрес {ip} пингуется')
    else:
        print (f'Адрес {ip} не пингуется')