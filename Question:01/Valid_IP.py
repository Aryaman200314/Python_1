def valid_IP(ip):
    ip_list = ip.split('.')

    if len(ip_list) != 4:
        return "Not a valid IP (Does not follow IPv4 formatting)"
    
    for n in ip_list:
        if not n.isdigit():  
            return "Not a valid IP (Contains non-numeric characters)"
        
        num = int(n)
        if num < 0 or num > 255:
            return "Not a valid IP (IP out of range)"
    ip_parts = tuple(map(int, ip_list))

    if (ip_parts[0] == 10) or \
       (ip_parts[0] == 172 and 16 <= ip_parts[1] <= 31) or \
       (ip_parts[0] == 192 and ip_parts[1] == 168):
        return "Valid Private IP"
    
    return "Valid Public IP"


ip = input("Enter the IP address: ")
print(valid_IP(ip))
