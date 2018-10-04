def bincon (decimal):
	print("BASE 10 DECIMAL: ",decimal)
	bin_str =""
	for i in range(8):
		binary = str(decimal % 2);
		print (binary," ")
		decimal = decimal // 2;
		bin_str = str(bin_str) + binary;
	print(bin_str)
	bin_str = "".join(reversed(bin_str))
	print(bin_str)
	print()
	
def main():
	done = 0
	while (done >= 0):
		print ("Type a value less than 0 to exit.",end='')
		dec	= input("Input a base 10 number less than 256.")
		dec = int(dec)
		bincon(dec)
	
main()	
	
	
