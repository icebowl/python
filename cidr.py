#cidr.py cwc
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
    subnet_return = [0,0,0,0]
    subnet_return[0] = int(bin_dec(subnet_list[0]))
    subnet_return[1] = int(bin_dec(subnet_list[1]))
    subnet_return[2] = int(bin_dec(subnet_list[2]))
    subnet_return[3] = int(bin_dec(subnet_list[3]))
    return subnet_return

def main():
    subnet = [0,0,0,0]
    print ("Input a CIDR value (32 to 1) : ",end="")
    cidr = input()
    subnet = cidr_subnet(cidr)
    print(subnet)

main()

"""
This python code takes a CIDR input , converts it to binary, then separates
the bits into four binary octets.  The binary octets are converted to decimal.
This code will be used to caluate network ids and broadcast addresses.
"""
