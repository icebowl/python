# your code goes here
'''
Input a grade number (9 - 12) and print 
Freshman, Sophomore, Junior, Senior. 
If it is not in [9-12], print Not in High School.
'''
g = int(input("What grade are you in ? "))
if(g == 9):
 print("Freshman")
elif (g==10): 
 print("Sophomore")
elif (g==11): 
 print("Junior")
elif (g==12): 
 print("Senior")
else:
 print("Not in High School.")
