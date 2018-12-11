# ipv4-cidr.py cwc

def cidr_subnet(cidr):
    n = 32 - int(cidr) #n counts the bits from left to right
    v = 32 # v is subtracted until v is 0
    subnet_string = ""
    while (v > 0):
        if(v % 8 == 0 and v != 32):
            subnet_string = subnet_string + "."
        if(v > n):
            subnet_string = subnet_string  + "1"
        else:
            subnet_string = subnet_string  + "0"
        v = v -1
    subnet_list = subnet_string.split(".")
    subnet_return = [0,0,0,0]
    subnet_return[0] = int(bin_dec(subnet_list[0]))
    subnet_return[1] = int(bin_dec(subnet_list[1]))
    subnet_return[2] = int(bin_dec(subnet_list[2]))
    subnet_return[3] = int(bin_dec(subnet_list[3]))
    return subnet_return

def get_ip_cidr_input():
    ipv4 = [0,0,0,0]
    subnet = [0,0,0,0]
    print ("Input a IPV4 CIDR as follows (192.168.1.10/24) : ",end="")
    ipv4_cidr_string = input()
    ipv4_temp = ipv4_cidr_string.split("/")
    print ("cidr",ipv4_temp[1])
    subnet = cidr_subnet(ipv4_temp[1])
    print ("subnet",subnet)
    #print (ipv4_temp)
    #print(ipv4_cidr_string)
    ipv4 = ipv4_temp[0].split(".")
    print(ipv4)
    return ipv4, subnet

def bin_dec(b): # b is a binary string
    d = 0 # d is the return decimal value (base 10) .
    i = 0 #i is the index of b string
    for n in range (len(b),0,-1):
        if (b[i] == "1"):
            d = d + (2**(n-1))
        i = i + 1
    return d


def main():
    ipv4 = [0,0,0,0]
    subnet = [0,0,0,0]
    ipv4,subnet = get_ip_cidr_input()
    #subnet = cidr_subnet(cidr)
    print(ipv4)
    print(subnet)

main()

"""
This python code takes a CIDR input , converts it to binary, then separates
the bits into four binary octets.  The octets from binary to decimal.

"""
