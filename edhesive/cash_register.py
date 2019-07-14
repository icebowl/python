'''
nsion: Cash Register Program
1 1 unread reply. 1 1 reply.

In CodeSkulptor, write a cash register program that calculates change for a restaurant of your choice. 
Your program should include:

    Ask the user to input the cost of 3 items purchased by the customer*
    Tell the user the total cost of the items purchased
    Ask the user to input the amount paid by the customer
    Calculate and print the amount of change to be given to the customer

*Hint: What data type will you need to use to deal with money (decimal numbers)?

Then, save your program and post the link to it into the discussion below.

After you post, you will be able to see the programs submitted by other students. 
Look through their programs and reflect: How are the programs similar to yours? 
How are they different?

'''
import math
print("Input the amount of three items.")
item1 = float(input("* Item 1 : "))
item2 = float(input("* Item 2 : "))
item3 = float(input("* Item 3 : "))

totalitems = round(item1 + item2 + item3,2)
print ("Total cost of all items " + str(totalitems))

paid = float(input("Amount paid : "))

change = round(paid-totalitems,2)

print ("Change = "+str(change))

