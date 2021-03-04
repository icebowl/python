import random
print(" DEBUG OUTPUT ")
matrix = [ ['0', '1', '2','3','4'],  
   ['5', '6', '7','8','9'  ],  
   ['a', 'b', 'c','d','e'  ], 
   ['f', 'g', 'h','i','j'  ], 
   ['k', 'l', 'm','n','o'  ],
   ]
   

for i in range(len(matrix)) :  
	for j in range(len(matrix[i])) :  
		print(matrix[i][j], end=" ") 
	print()   

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
	print("ROW = "+str(n+1)+" KEY = "+str(rowkey[n])) 
	
print("ROW CODE DEBUG ")
print(rowchr)

inkey = ['*','*','*','*','*']
correctinputs = 0
for n in range (0,5):
	inkey[n] = input("Input ROW "+str(n+1)+" CHARATER ")
	if (inkey[n] == rowchr[n]):
		correctinputs = correctinputs + 1
		
print(correctinputs)
	
	
	
