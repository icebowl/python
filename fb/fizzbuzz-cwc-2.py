import sys
for n in range(1,101):
	if n % 3 == 0:
		sys.stdout.write("Fizz")
		if n%5 != 0:
			sys.stdout.write("\n")
	if n % 5 == 0:
		sys.stdout.write("Buzz\n")
	if n % 3 != 0 and n % 5 != 0:
		print(n)

