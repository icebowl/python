'''
When we read code and predict its output,
it is called tracing code.

For this lesson you will come up with your 
own challenging algorithm for other students to trace. 
It must contain at least 5 - if statements and use at 
least one AND or OR boolean condition. 
Run it in the sandbox, 
then copy and paste your code in Piazza for 
other students to try.

For this challenge try reading 3 or 4 other students' 
code - trace the code and predict what it outputs, 
then run it in the sandbox to see if you got it right.
'''
import random
iterations = 100
count = 0
count_mn = 0
count_mx = 0
count_md = 0
rv = 0
done = False
'''
Write code to explain what this algorithm does along with
describing the variable names.
'''
while(done==False):
 mn = int(input("Input a minimum integer value: "))
 mx = int(input("Input a maximum integer value: "))
 if(mn<mx):
  done=True
md = int((mx - mn)/2)
while(count <= iterations):
 rv = random.randint(mn,mx)
 if (count % 10 == 0 and count != 0):
  print()
 print (str(rv)+str(" "),end="")
 count = count+1
 if(rv == mn):
  count_mn = count_mn + 1
 if(rv == mx):
  count_mn = count_mx + 1
 if(rv == md):
  count_md = count_md + 1
'''
Write code to explain what this output represents.
'''
print("mn , count_mn , md, count_md, mx, count_mx")
print(mn,count_mn,md,count_md,mx,count_mx)
