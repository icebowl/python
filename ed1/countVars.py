n = int(input("Enter a number, -1 to stop"))
sum = 0
while (n != -1):
    print ("You entered: " + str(n))
    n = int(input("Enter a number, -1 to stop"))
    sum = sum + n
print ("Sum of numbers entered: " + str (sum))
