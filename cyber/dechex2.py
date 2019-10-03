# dechex2.py cwc
def hexcon(num):
	h16s = ""; h1s =""; temp =""
	h16 = int(num/16)
	temp = str(chr(87+h16))
	print("chr ",temp)
	h1 = num % 16 
	temp = str(chr(87+h1))
	print("chr ",temp)
	h16s = str(h16); h1s = str(h1)
	h = h16s + h1s
	return h
	
def main():
	hs = "";hs2 = ""
	hs = hexcon(147);hs2 = hexcon(157)
	print(147,hs,157,hs2)
	
main()
