#python
from random import randint
alpha = ['a','b','c','d','e']
count = 0
while True:
	i = randint(0, 4)
	#print (i)
	print(alpha[i],end="")
	count = count +1
	if (count > 100):
		break
