def bin_dec(b): # b is a binary string
    d = 0 # d is the return decimal value (base 10) .
    i = 0 #i is the index of b string
    for n in range (len(b),0,-1):
        if (b[i] == "1"):
            d = d + (2**(n-1))
        i = i + 1
    return d

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
    return subnet_return

def main():
    subnet = [0,0,0,0]
    print ("Input a CIDR value (32 to 1) : ",end="")
    cidr = input()
    subnet = cidr_subnet(cidr)
    o1 = int(bin_dec(subnet[0]))
    o2 = int(bin_dec(subnet[1]))
    o3 = int(bin_dec(subnet[2]))
    o4 = int(bin_dec(subnet[3]))
    print ("SUBNET = "+str(o1)+"."+str(o2)+"."+str(o3)+"."+str(o4))
    print(subnet)

main()
