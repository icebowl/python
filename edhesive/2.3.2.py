# your code goes here
'''
Enter the Feet for the first piece of fabric: 3
Enter the Inches for the first piece of fabric: 11

Enter the Feet for the second piece of fabric: 2
Enter the Inches for the second piece of fabric: 5
'''

feet1 = int(input("Enter the Feet for the first piece of fabric: "))
inches1 = int(input("Enter the Inches for the first piece of fabric: "))

feet2 = int(input("Enter the Feet for the second piece of fabric: "))
inches2 = int(input("Enter the Inches for the second piece of fabric: "))

totalinches = inches1 + inches2 + feet1 *12 + feet2 *12
tf = int(totalinches / 12)
ti = int(totalinches % 12)
print("Feet: "+str(tf)+" Inches: "+str(ti))

