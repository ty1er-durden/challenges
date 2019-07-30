"""
Write a program that will test if an IP address
is in a given network:

(1) Take input as a string:
    (a) An arbitrary network in CIDR notation (e.g. 192.168.1.0/25)
    (b) An arbitrary IP address
    Display back to user:
    (a) Network Address
    (b) Subnet mask
    (c) IP address
(2) Convert the subnet mask to an integer such that binary operations can be perfomed on it
(3) Convert the network address to an integer
(4) Convert the candidate address to an integer (same procedure as above)
(5) Compare (3) and (4) to determine if ip is in network
"""

# (1)
net = input("Enter network using CIDR notation: ")
candidate_address = input("Enter an IP address: ")

net_address, length = net.split("/")
length = int(length)
print("Network Address:", net_address)
print("Subnet Length:", length)
print("IP Address:", candidate_address)

# (2)
mask = int("1" * length + "0" * (32 - length), 2)

# (3)
octets = net_address.split(".")
net_ip = 0
for n in range(4):
    net_ip += int(octets[3 - n]) << (8 * n)

# (4)
octets = [int(octet) for octet in candidate_address.split(".")]
candidate_ip = 0
for n in range(4):
    candidate_ip += octets[3 - n] << (8 * n)

# (5)
if candidate_ip & mask == net_ip:
    print(f"{candidate_address} belongs to {net_address}/{length}")
else:
    print(f"{candidate_address} does NOT belong to {net_address}/{length}!")
