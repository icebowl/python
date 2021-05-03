'''
    at least 5 questions
    at least 2 if-elif-else statements
    the use of the random module and randomly generated numbers 
'''


import random

def print_matrix(m):
	for i in range(len(m)) :  
		print("     ",end="")
		for j in range(len(m[i])) :  
			print(m[i][j], end=" ") 
		print()   

def build_matrix(m):

	for i in range(len(m)) :  
		for j in range(len(m[i])) :  
			numberletter = random.randint(0,1)
			if (numberletter == 0):
				n = chr(random.randint(48, 57)) 
			else:
				n = chr(random.randint(97, 112)) 
			#print(n, end=" ") 
			m[i][j] = n
		
	return m

def main():
	done = False
	m = [ ['*', '*', '*','*','*'],  
   ['*', '*', '*','*','*'], 
   ['*', '*', '*','*','*'],
   ['*', '*', '*','*','*'],
   ['*', '*', '*','*','*'],
   ]
	while(done == False):
		m = build_matrix(m)
		print("     MATRIX CODES")
		print_matrix(m)
		print("\n     Here is your security HUMAN checking matrix.")
		print("     Do you want to keep this matrix? (y or n) ",end="")
		keep = input("")
		keep = keep.lower()
		keep = keep[0]
		print ("keep", keep)
		if (keep == 'y'):
			done = True
		else:
			m = build_matrix(m)
	rowkey = [-1,-2,-3,-4,-5]
	rowchr  = ['*','*','*','*','*']

	print(" KEY CODE ")

	# create key inputs
	for n in range (0,5):
		rowkey[n] = random.randint(0,4)
		rowchr[n] = m[n][rowkey[n]]
		print("ROW = "+str(n+1)+" KEY = "+str(rowkey[n]+1)) 

	inkey = ['*','*','*','*','*']
	correctinputs = 0
	for n in range (0,5):
		inkey[n] = input("Input ROW "+str(n+1)+" CHARATER ")
		if (inkey[n] == rowchr[n]):
			correctinputs = correctinputs + 1
	if(correctinputs == 5):
		print("WELCOME TO THE PLANET. You are a HUMAN!")
	elif (correctinputs == 4):
		print("You are a HUMAN but you missed ONE code")
	if(correctinputs == 3):
		print("You are a HUMAN but you need to learn how to enter codes correctly.")
	elif(correctinputs== 2 or correctinputs == 1):
		print("Try again or get another HUMAN")
	elif (correctinputs == 0):
		print(" ? ")
	#print(correctinputs)
	
if __name__ == "__main__":
	main()
