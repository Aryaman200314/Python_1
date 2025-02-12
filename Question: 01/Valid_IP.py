def valid_IP(ip):
    ip_list = ip.split('.')
    if len(ip_list) != 4:
        return "Not an valid IP (Does not follow IPV4 formating)"
    for n in ip_list:
        if n.isdigit() == False:
            return "Not an valid IP (There is an Alphabet in IP)"
        if int(n) < 0 or int(n) > 255:
            return "Not an valid IP (IP out of range)"
    return "Valid IP"



ip = input("Enter the IP address: ")
print(valid_IP(ip))