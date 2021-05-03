import random
#print(" DEBUG OUTPUT ")
matrix = [ ['0', '1', '2','3','4'],  
   ['5', '6', '7','8','9'  ],  
   ['a', 'b', 'c','d','e'  ], 
   ['f', 'g', 'h','i','j'  ], 
   ['k', 'l', 'm','n','o'  ],
   ]
   
#for i in range(len(matrix)) :  
#	for j in range(len(matrix[i])) :  
#		print(matrix[i][j], end=" ") 
#	print()   

print("\n MATRIX CODES\n")
rowkey = [-1,-2,-3,-4,-5]
rowchr  = ['*','*','*','*','*']

for i in range(len(matrix)) :  
	for j in range(len(matrix[i])) :  
		numberletter = random.randint(0,1)
		if (numberletter == 0):
			n = chr(random.randint(48, 57)) 
		else:
			n = chr(random.randint(97, 112)) 
		print(n, end=" ") 
		matrix[i][j] = n
	print()
print(" KEY CODE ")


for n in range (0,5):
	rowkey[n] = random.randint(0,4)
	rowchr[n] = matrix[n][rowkey[n]]
	print("ROW = "+str(n+1)+" KEY = "+str(rowkey[n]+1)) 
	
#print("ROW CODE DEBUG ")
#print(rowchr)

inkey = ['*','*','*','*','*']
correctinputs = 0

inkey[0] = input("Input ROW 1 CHARACTER ")
if (inkey[0] == rowchr[0]):
	correctinputs = correctinputs + 1
inkey[1] = input("Input ROW 2 CHARACTER ")
if (inkey[1] == rowchr[1]):
	correctinputs = correctinputs + 1
inkey[2] = input("Input ROW 3 CHARACTER ")
if (inkey[2] == rowchr[2]):
	correctinputs = correctinputs + 1
inkey[3] = input("Input ROW 4 CHARACTER ")
if (inkey[3] == rowchr[3]):
	correctinputs = correctinputs + 1
inkey[4] = input("Input ROW 5 CHARACTER ")
if (inkey[4] == rowchr[4]):
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

question = input("Do you think this system will work?")
if(question == "y" or question == "Y"):
    print("THANK YOU . WHY")
else:
    print("WHY")
	
	
