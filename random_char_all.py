# save this file as random int.py
from random import randint
def randlist(r,usedlist,done):
	alpha = ['!','"','#','$','%','&','\'','(',')','*',
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
	#print (c)
	usedlist[r] = 1
	sum = 0
	for i in range(len(usedlist)):
		sum = sum + usedlist[i]
		if sum == 94:
			done = True
	return c,usedlist,done
	
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
	done = False
	while done == False:
		r = randint(0,93)
		if used[r] == 0:
			c,used,done = randlist(r,used,done)
			#print (r,c,used,done)
			print(c,end='')
	
main()
