def ip_to_num(ip):
    b = ''
    for i in ip.split('.'):
        b += format(int(i), "08b")
    return int(b,2)

def num_to_ip(num):
    binary = bin(num).lstrip('0b').zfill(32)
    ip=[]
    for i in range(0, len(binary), 8):
        octet = binary[i:i+8]
        ip.append(str(int(str(octet),2)))
    return '.'.join((ip))

print(ip_to_num('176.16.0.1'))
print(num_to_ip(2953838593))
