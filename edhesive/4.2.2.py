#cwc
sum = 0; count = 0;
while (sum < 100):
    n = float(input("Input a number to be added to the sum "+str(sum)+" ."))
    sum = sum + n
    print("Sum = "+str(sum))
    count = count + 1
print ("The sum is "+str(sum)+" with a count of "+str(count)+".")
