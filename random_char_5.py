# save this file as random int.py
from random import randint
def randlist(r,usedlist,done):
	alpha = ['!','\"','#','$','%','&',''','(',')','*',
	         '+',',','-','.','/','0','1','2','3','4',
	         '5','6','7','8','9',':',';','<','=','>',
	         '?','@','A','B','C','D','E','F','G','H',
	         'I','J','K','L','M','N','O','P','Q','R',
	         'S','T','U','V','W','X','Y','Z','[','\\',
	         ']','^','_','`','a','b','c','d','e','f',
	         'g','h','i','j','k','l','m','n','o','p',
	         'q','r','s','t','u','v','w','x','y','z',
	         '{','|','}','~']
	        
	c = alpha[r]
	sum = 0
	for i in range(len(usedlist)):
		sum = sum +usedlist[i]
	# print (sum)
	if 
	
	return c, usedlist ,done
	
def main():
	used = [0,0,0,0,0,0,0,0,0,0,
	        0,0,0,0,0,0,0,0,0,0,
	        0,0,0,0,0,0,0,0,0,0,
	        0,0,0,0,0,0,0,0,0,0,
	        0,0,0,0,0,0,0,0,0,0,
	        0,0,0,0,0,0,0,0,0,0,
	        0,0,0,0,0,0,0,0,0,0,
	        0,0,0,0,0,0,0,0,0,0,
	        0,0,0,0,0,0,0,0,0,0,
	        0,0,0,0]
	done = True
	while True:
		r = randint(0,5)
		c = randlist(r,used,done)
		print (used)
		# print(c,end="")
main()
