
def get_intf_ip_dict_free_cfg(filename):
    intf_ip_dict = {}

    with open[filename] as f:
        for line in f:
            if line.startswitch("interface"):
                intf = line.split()[-1]
            elif line.startswitch(" ip address"):
                ip = line.split()[-2]
                intf_ip_dict[intf] = ip


config_list = ["config_r1.txt", "config_sw1.txt","config_r2.txt"]
print(intf_ip_dict)