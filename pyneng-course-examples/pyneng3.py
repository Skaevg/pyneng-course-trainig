acceess = ["switchport mode acceess",
    "switchport acceess vlan",
    "switchport nonegotilate",
    "spaning-tree portfast",
    "spaning-tree bpduguard enable"]
print(acceess)
print("\n".join(acceess)) # добавление знака enter в конце списка.

vlans = [10, 100, 290, 42, 202]
vlans.pop()
print(vlans)
vlans.pop(0)
print(vlans)