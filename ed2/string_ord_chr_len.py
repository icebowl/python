#cwc 
def printIt(aa):
	print("aa ",aa)
	print("aa[3] ",aa[3])
	print("aa[-1] ",aa[-1]) 
	print("aa[2:4] ",aa[2:4]) 
	print("aa[1:] ",aa[1:]) 
	print("aa[:3] ",aa[:3])
	print("aa[:] ",aa[:]) 
	
	for i in range (len(aa)):
		print(chr(aa[i]))

def printString(inputString): 
	iS = inputString;
	length = len(inputString); 
  
	for i in range(length): 
		print(i," iS ", iS[:i])
	
	for j in range(length):
		print("ord ", iS[j],ord(iS[j]))

def main():
	ABCString = "_ABCDEFGHIJKLMNOPQRSTUVWXYZ"; 
	a = (33,34,35,36,37,38,39,40)
	printIt(a)
	printString(ABCString)
if __name__ == '__main__':
	main()

'''
https://www.python.org/ftp/python/doc/1.1/quick-ref.1.1.html
'''
