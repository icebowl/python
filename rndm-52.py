#65536.py cwc
import random
for i in range (0,52):
 n =  random.randint(0,51)
 print(n," ",end="")
 if(i != 0 and i % 10 == 0):
	 print(" * ")
print(i," * * * ")


