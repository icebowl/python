import sys
for n in range(1,101):
	if n % 3 == 0:
		print("Fizz",end="")
		if n%5 != 0:
			print()
	if n % 5 == 0:
		print("Buzz")
	if n % 3 != 0 and n % 5 != 0:
		print(n)

