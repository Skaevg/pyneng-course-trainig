# table = [['100','a1b2.s2g3.f4g5.h6j7','DYNAMIC', 'GI0/1'],
#          ['200','a1b2.s2g3.f4g5.h6j7','DYNAMIC', 'GI0/2'],
#          ['300','a1b2.s2g3.f4g5.h6j7','DYNAMIC', 'GI0/3'],
#          ['400','a1b2.s2g3.f4g5.h6j7','DYNAMIC', 'GI0/4'],
#          ['500','a1b2.s2g3.f4g5.h6j7','DYNAMIC', 'GI0/5'],
# ]

# for vlan,mac, type, intf in table:
#     print(f"{vlan:10}{mac:25}{intf:20}")

vlans = [1,2,3,4,5]
vlans_str = []
for vl in vlans:
    vlans_str.append(str(vl))

vlans_str = [str(vl) for vl in vlans] # list comprehension 

data = ["11","2",'asd','20','b']
digits_only = []
for item in data:
    if item.isdigit():
        digits_only.append(int(item))
    
[int(item) for item in data if item.isdigit()] # list comprehension 

vlans = [[10,21,34],[101,151,115],[111,50,20]]
data = []
for vl_list in vlans:
    for vl in vl_list:
        data.append(vl)

[vl for vl_list in vlans for vl in vl_list] # list comprehension 
{vl for vl_list in vlans for vl in vl_list} # set comprehension 

r1 = {'IOS': '15.4',
      'IP': '10.159.13.2',
      'hostname': 'london_r1',
      'location': '21 New Globe Walk',
      'model': '4451'  }

new_r1 = {}
for key, value in r1.items():
    new_r1[key.lower()] = value

print(new_r1)

{key.lower(): value for key, value in r1.items()} # dict comprehension 

keys = "ios ip hostname".split()

{key: value for key, value in new_r1.items() if key in keys}
r1_filter = {}
for key, value in new_r1.items():
    if key in keys:
        r1_filter[key] = value

