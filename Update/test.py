new_address = "155.2.2.1"
add_to_iptables_commands = [
    f"sudo iptables -A FORWARD -p tcp --dport 80 -d {new_address} -j ACCEPT",
    f"sudo iptables -A FORWARD -p tcp --dport 443 -d {new_address} -j ACCEPT",
    f"sudo iptables -A FORWARD -p udp --dport 80 -d {new_address} -j ACCEPT",
    f"sudo iptables -A FORWARD -p udp --dport 443 -d {new_address} -j ACCEPT",
]

for i in add_to_iptables_commands:
    print(i)
