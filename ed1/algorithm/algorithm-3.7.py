'''
For this lesson, you will come up with your own challenging algorithm 
for other students to trace. It must contain at least 5 if statements 
and use at least one AND or OR boolean condition.

Note: Elif or else statements will not count - 
your statements must be if statements. 
Each if statement should use a unique variable name.

'''
import random
iterations = 100
count = 0
count_mn = 0 #  count minimum
count_mx = 0 #  count maximum
count_md = 0 #  count middle
rv = 0
count1000 = 0
done = False # boolean

while(done==False):
	mn = random.randint(0,100)
	mx = random.randint(0,1000)
	if(mn<mx):
		done=True
	md = int((mx + mn)/2)
#end while(done==False):

while(count <= iterations-1):
	rv = random.randint(mn,mx)
	#if (count % 10 == 0 and count != 0):
	#	print()
	if (rv == 1000):
		count1000 = count1000 +1
	print (str(rv)+str(" "),end="")
	count = count+1
	if(rv == mn):
		count_mn = count_mn + 1
	if(rv == mx):
		count_mx = count_mx + 1
	if(rv == md):
		count_md = count_md + 1

#print("\nmn , count_mn , md, count_md, mx, count_mx")
#print(mn,count_mn,md,count_md,mx,count_mx)
print("* * * * * * * * * * * * * * * * * *")
print("* MINIMUM = ",mn,"COUNT = ",count_mn)
print("* MIDDLE  = ",md,"COUNT = ",count_md)
print("* MAXIMUM = ",mx,"COUNT = ",count_mx)

'''
 #mn = int(input("Input a minimum integer value: "))
 #mx = int(input("Input a maximum integer value: "))
'''
