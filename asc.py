def main():
	for i in range (1,256):
		i = int(i)
		c = chr(i)
		print("[",i,"=",c,"]",end="")
		if (i % 10 == 0):
			print("\n")
main()
