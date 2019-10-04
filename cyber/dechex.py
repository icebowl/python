# dechex.py cwc kenny
def hexcon(num):
	key = "0123456789abcdef" # hex key
	h = ""
	h16 = int(num/16)
	h1 = num % 16
	h = key[h16]+ key[h1]
	return h
	
def main():
	hs = ""
	for i in range(0,256):
		hs = hexcon(i)
		print(i,hs)
	
main()
