# basecon.py cwc
def hexcon(num):
	key = "0123456789abcdef" # hex key
	h = ""
	h16 = int(num/16)
	h1 = num % 16
	h = key[h16]+ key[h1]
	return h

def bincon(num,addSpace):
	n = num
	s = addSpace
	#print(n,s) #debug
	#print(n," = ",end="")
	d = 128
	binString ="" #create a string called binString
	for i in range(0,8):
		q = int(n / d)
		r = int(n % d)
		n = r
		d = int(d / 2)
		binString = binString+str(q)
		if(s == 1 and i == 3):
			binString = binString + " "
	#print(binString)
	return binString
	
def main():
	bs = ""
	for i in range(0,256):
		bs = bincon(i,1)
		hs = hexcon(i)
		c = chr(i)
		print(i,bs,hs,c)
	
main()
