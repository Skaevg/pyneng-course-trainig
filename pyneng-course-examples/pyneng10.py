from re import I


result = {}
{
    "Ethernet0/0": {"mtu": 1500, "ip": "192.168.100.1/24"},
    "Ethernet0/1": {"mtu": 1500, "ip": "192.168.200.1/24"},
    # "Ethernet0/1": 1500,
    # "Ethernet0/1": 1500,
}

with open('sh_ip_interface.txt') as f:
    for line in f:
        line = line.rstrip()
        if 'line protocol' in line:
            intf = line.split()[0]
            result[intf] = {}
        elif "Internet address" in line:
            ip = line.split()[-1]
            result[intf]["ip"] = ip #записываем в словарь 
        elif "MTU" in line:
            mtu = line.split()[2]
            print(intf, ip, mtu) # вывод двух переменных т.к интф уже создан и поэтому соответствует.
            result[intf]["mtu"] = mtu # result ключ = значение


print(result)


