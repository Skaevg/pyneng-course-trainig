# mac = ["aabb:cc80:7000", "aabb:dd80:7340", "aabb:ee80:7000", "aabb:ff80:7000"]
# result = []

# for i in mac:
#     i2 = i.replace(":",".")
#     result.append(i2)
# print(result)

ip = input("Введите ip (XXX.XXX.XXX.XXX): ")
ip_address = ip.split(".")

correction_ip = True

if len(ip_address) != 4:
    correction_ip = False
else:
    for int_ip in ip_address:
        if not (int_ip.isdigit() and int(int_ip) in range(256)):
            correction_ip = False
            break
ip_address0 = int(ip_address[-1])


if ip == "255.255.255.255":
    print("local broadcast")
elif ip == "0.0.0.0":
    print("unassigned")
elif ip_address0 in range(1,223):
    print("multicast")
elif ip_address0 in range(224,255):
    print("unicast")
else:
    print ("unused")


