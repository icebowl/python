def GPAcalc(n,w):
    if(w == "1"):
        if(n == "A" or n == "a"):
            return 5
        elif(n == "B" or n == "b"):
            return 4
        elif(n == "C" or n == "c"):
            return 3
        elif(n == "D" or n == "d"):
            return 2
        elif(n == "F" or n == "f"):
            return 1
        else:
            return "Invalid"
    elif(w == "0"):
        if(n == "A" or n == "a"):
            return 4
        elif(n == "B" or n == "b"):
            return 3
        elif(n == "C" or n == "c"):
            return 2
        elif(n == "D" or n == "d"):
            return 1
        elif(n == "F" or n == "f"):
            return 0
        else:
            return "Invalid"
    else:
        return "Invalid"

total = int(input("How many Classes are you taking? "))
x = 0
gpa = 0
while(x < total):
    n = input("\nEnter your Letter Grade: ")
    w = input("Is it weighted?(1 = yes, 0 = no) ")
    g = GPAcalc(n,w)
    if(g == "Invalid"):
        print("Your GPA score is Invalid")
    else:
        gpa = gpa + g
    x = x + 1
    print("x ",x," total ",total)
print("Your GPA score is: " + str(gpa/total) + ".0.")
