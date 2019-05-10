#!/usr/bin/python
import sys
def split(word):
    return [char for char in word]

def ConvertHex(string):
    li = list(string.split(" "))
    print('string length',len(string))
    chrList =[]
    for n in range(len(string)):
        #format(ord("c"), "x")
        chrlist[n] = string[n]
        print(chrlist[n])
    return chrlist

print (len(sys.argv))
print (str(sys.argv))
n = len(sys.argv)
print(n)
chrList =[]
chrList = ConvertHex(sys.argv[1])
print(chrList)


'''
def bincon (decimal):
	print("BASE 10 DECIMAL: ",decimal)
	bin_str =""
	for i in range(8):
		binary = str(decimal % 2);
		print (binary," ")
		decimal = decimal // 2;
		bin_str = str(bin_str) + binary;
	print(bin_str)
	#bin_str = "".join(reversed(bin_str))
	print(bin_str[::-1] )
	print()

def main():
	print ("Type a value less than 0 to exit.",end='')
	done = 0
	while (done >= 0):
		dec	= input("Input a base 10 number less than 256.")
		dec = int(dec)
		bincon(dec)

main()


'''
