import random

def generate_random_ip():
    return f"192.168.1.{random.randint(0,20)}"

def check_firewall_rules(ip, rules):
    for rule_ip, action in rules.items():
        if ip ==rule_ip:
            return action
    return "ALLOW"

def main():
    firewall_rules ={
        "192.168.1.1": "BLOCK",
        "192.168.1.6": "BLOCK",
        "192.168.1.19": "BLOCK",
        "192.168.1.12": "BLOCK",
        "192.168.1.8": "BLOCK",
        "192.168.1.15": "BLOCK"
    }
    
    for _ in range(12):
        ip_address = generate_random_ip()
        action = check_firewall_rules(ip_address, firewall_rules)
        random_number = random.randint(0,9999)
        print(f"IP_ADD: {ip_address}, ACTION: {action}, SYSTEM_ID: {random_number}")
    
    
if __name__ == "__main__":
    main()
