from netaddr import *

ipv4_addr_space = IPSet(['0.0.0.0/0'])
private = IPSet(['10.0.0.0/8', '172.16.0.0/12', '192.0.2.0/24', '192.168.0.0/16', '239.192.0.0/14'])
reserved = IPSet(['225.0.0.0/8', '226.0.0.0/7', '228.0.0.0/6', '234.0.0.0/7', '236.0.0.0/7', '238.0.0.0/8', '240.0.0.0/4'])

orlando_home = IPSet(['192.168.1.0/24'])

unavailable = reserved | private
available = ipv4_addr_space ^ unavailable | orlando_home

emory  = IPSet(['170.140.0.0/16'])

office_vpn = available ^ emory

print(",".join(map(str, office_vpn.iter_cidrs())))
