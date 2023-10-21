from re import T


cmd = "interface Gi0/0"
print(cmd.startswith("interface")) # начинается строка
print(cmd.startswith("test")) # false
print(cmd.startswith("inteface")) # false
print(cmd.startswith("nterface")) # false
print(cmd.startswith("nterface", 1)) # true
cmd2 = "switchport mode acceess"
print(cmd2.count("s")) # кол-во совпадений 3
print(cmd2.count("port")) # 1
print(cmd2.find("mode")) # 11 Находит индекс, где начинается моде
print(cmd2.find("test")) # -1
find_word = 'mode'
print(cmd2.find(find_word))
index = cmd.find(find_word)
print(cmd2[index:])
print(cmd2[index:index + len(find_word)])
print(cmd2.find("o")) #первое совпадение где встречается по индексу
cmd2.replace("Gi", "Fa") #замена строки создает новую строку, для сохранения надо в новую строку вписывать.
new_cmd = cmd2.replace("Gi", "Fa")
cmd2.strip()# убирает все whitespace символы типа "][][/n/ninterface Gi0/0[][/t" выводя только ("interface Gi0/0")
cmd2.lstrip()# убирай слева
cmd2.rstrip()# убирай справа
cmd3 = "switchport trunk allowed vlan 1,2,3,4,5\n"
print(cmd3.split())# разбивает на слова. ['switchport', 'trunk', 'allowed', 'vlan', '1,2,3,4,5']

tunnel_template = """
interface Tunnel {}
    ip address {}
    ip mtu 1416
    ip ospf hello-interval 5
    tunnel source {}
    tunnel protection ipsec profile DMVPN
"""
print(tunnel_template.format("1","192.168.123.09 255.255.255.0", "Gi0/0"))


tunnel_template = """
interface Tunnel {0}
    ip address {2}
    ip mtu 1416
    ip ospf hello-interval 5
    tunnel source {1}
    tunnel protection ipsec profile DMVPN
"""
print(tunnel_template.format("1", "Gi0/0", "192.168.123.09 255.255.255.0"))

tunnel_template = """
interface Tunnel {tun}
    description Tunnel {tun}
    ip address {ip_addr}
    ip mtu 1416
    ip ospf hello-interval 5
    tunnel source {sour}
    tunnel protection ipsec profile DMVPN
"""
print(tunnel_template.format(tun="1", sour="Gi0/0", ip_addr="192.168.123.09 255.255.255.0"))

ip_template = "{} {} {} {}"
ip_template.format(1,2,3,4)
