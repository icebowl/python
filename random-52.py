#random-52.py python3 cwc
# Run this code and keep track of how many time you need to run the code
# to get a '0' as the first integer displayed
import random
for i in range (1,53): 
 n =  random.randint(0,51)
 print(n," ",end="")
 if(i % 10 == 0):
	 print(" * ")
print("\n\t\t",i,"<- last i - - - \n\n")


