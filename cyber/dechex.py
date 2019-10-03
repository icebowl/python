# dechex.py cwc
def hexcon(num):
	#print(num," in dechex funtion ",end="")
	h = "";hs16 = "##";hs1="$$" #strings
	h16 = int(num/16)
	hs16 = str(h16)
	if(h16 > 9):
		print("h16 is greater than 9")
	h1 = num % 16
	hs1 = str(h1)
	if(h1 > 9):
		print("h11 is greater than 9")
	h = hs16+hs1
	return h
	
def main():
	hs = ""
	for i in range(147, 160):
		hs = hexcon(i)
		print(i,hs)
	
main()
