def bin_dec(b): # b is a binary string
    d = 0 # d is the ending decimal value (base 10) . Asume d is '0'
    i = 0 #i is the index of b string
    for n in range (len(b),0,-1):
        if (b[i] == "1"):
            d = d + (2**(n-1))
        i = i + 1
    return d

def cidr_subnet(cidr):
    n = 32 - int(cidr)
    v = 32
    subnet_string = ""
    while (v > 0):
        if(v % 8 == 0 and v != 32):
            subnet_string = subnet_string + "."
        if(v > n):
            subnet_string = subnet_string  + "1"
        else:
            subnet_string = subnet_string  + "0"
        v = v -1
    subnet_list = subnet_string
    subnet_list = subnet_list.split(".")
    print(subnet_string)
    print(subnet_list)
    o1 = int(bin_dec(subnet_list[0]))
    o2 = int(bin_dec(subnet_list[1]))
    o3 = int(bin_dec(subnet_list[2]))
    o4 = int(bin_dec(subnet_list[3]))
    print ("SUBNET = "+str(o1)+"."+str(o2)+"."+str(o3)+"."+str(o4))

def main():
    subnet = [0,0,0,0]
    print(subnet)
    print ("Input a CIDR value (32-1) : ",end="")
    cidr = input()
    cidr_subnet(cidr)
main()
