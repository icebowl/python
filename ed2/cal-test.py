import calendar
def leap_year(y):
    calendar.isleap(y)

def number_of_days(m):
    if(m == "1" or m == "3" or m == "5" or m == "7" or m == "8" or m == "12"):
        return "31"
    elif(m == "4" or m == "6" or m == "9" or m == "10" or m == "11"):
        return "30"
    else:
        return "28"

#def days_left(d,m,y):
    

print("Please enter a date")
d = input("Day: ")
m = input("Month: ")
y = input("Year: ")
print("Menu:")
print("1) Calculate the number of days in the given month.\n2) Calculate the number of days left in the given year.")
nd = input("")
if(nd == "1"):
    print(leap_year(y))
    #if(leap_year(y) == "True" and number_of_days(m) == "28"):
        #print(number_of_days(m) + 1)
elif(nd == "2"):
    print('y')
else:
    print("Invalid, try again")
