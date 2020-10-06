# cwc + edhesvie
def leap_year(y):
    if y % 4 == 0:
        return 1
    else:
        return 0

def number_of_days(m,y):
    y = leap_year(y)
    if (m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12):
        return 31
    elif (m == 4 or m == 6 or m == 9 or m == 11):
        return 30
    elif (m == 2):
        if (y == 1):
            return 29
        elif (y == 0):
            return 28

def days_left(d,m,y):
    days_remaining = 0
    for i in range(m,13):
        days_sum = number_of_days(m,y)
        days_remaining = days_remaining + days_sum
        print(i,days_remaining,days_sum)
        m = m+1
    return days_remaining - d

print("Please enter a date")
day = int(input("Day: "))
month = int(input("Month: "))
year = int(input("Year: "))

print("Menu:")
print("1)    Calculate the number of days in the given month.")
print("2)    Calculate the number of days left in the given year.")
menu = int(input())
if (menu == 1):
    days_sum = number_of_days(month,year)
    print(days_sum)
elif (menu == 2):
    days_remaining_sum = days_left(day, month, year)
    print(days_remaining_sum)
