import random
a = [ ['0', '1', '2','3','4'  ],  
   ['5', '6', '7','8','9'  ],  
   ['a', 'b', 'c','d','e'  ], 
   ['f', 'g', 'h','i','j'  ], 
   ['k', 'l', 'm','n','o'  ],
   ]
   

for i in range(len(a)) :  
	for j in range(len(a[i])) :  
		print(a[i][j], end=" ") 
	print()   

print("\n**************\n")

for i in range(len(a)) :  
	for j in range(len(a[i])) :  
		numberletter = random.randint(0,1)
		if (numberletter == 0):
			n = chr(random.randint(48, 57)) 
		else:
			n = chr(random.randint(97, 112)) 
		print(n, end=" ") 
	print()
print(" KEY CODE ")
#rowkey = ['*','*','*','*','*']
rowkey = [-1,-2,-3,-4,-5]
for n in range (0,5):
	rowkey[n] = random.randint(0,4)
	print("ROW = "+str(n+1)+" KEY = "+str(rowkey[n])) 
	
	
print(rowkey)
