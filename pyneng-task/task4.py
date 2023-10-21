
# def generate_trunk_config(intf_vlan_mapping, trunk_template):
#     for intf,vlan in intf_vlan_mapping.items():
#         print(f"{intf}")
#         for template in trunk_template:
#             if template.endswith("vlan"):
#                 vlans = str(vlan)
#                 print(f"{template} {vlans}")
#             else: print(template)



trunk_mode_template = [
    "switchport mode trunk", "switchport trunk native vlan 999",
    "switchport trunk allowed vlan"
]

trunk_config = {
    "FastEthernet0/1": [10, 20, 30],
    "FastEthernet0/2": [11, 30],
    "FastEthernet0/4": [17]
}


def generate_trunk_config(trunk_config, trunk_mode_template):

    for key, value in trunk_config.items():
        template2 =""
        probel = ", "
        template_vlans = ""
        for template in trunk_mode_template:
            if template.endswith("vlan"):
                template2 += template + str(value)
            else: template2 += template + probel
        if template2.endswith("]"):
            template_vlans += str(template2)
        else: template_vlans = str(template2 + probel)  
        trunk_conf = {key: template_vlans}
        print(trunk_conf)

generate_trunk_config(trunk_config, trunk_mode_template)