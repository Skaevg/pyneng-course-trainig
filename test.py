from asyncio.windows_events import NULL


true_conf = ["Current configuration : 2033 bytes","Last configuration change at 13:11:59 UTC Thu Feb 25 2016",
"version 15.0","service timestamps debug datetime msec","service timestamps log datetime msec","no service password-encryption","hostname sw1","interface FastEthernet1/0"," switchport mode access"," switchport access vlan 20"," duplex auto","interface FastEthernet1/1"," switchport mode access"," switchport access vlan 30"," duplex auto","interface FastEthernet1/2"," switchport trunk encapsulation dot1q"," switchport trunk allowed vlan 400,500,600"," switchport mode trunk"," duplex auto","interface Vlan100"]
value_t = []
key_i = []
value_i = []
for i in true_conf:
    if i.startswith(" "):
        value_i.append(i)
        dict_t = dict(zip(key_i, value_i))
    elif not i.startswith(" "):
        key_i.append(i)
        dict_t = dict(zip(key_i, value_t))        
print(dict_t)