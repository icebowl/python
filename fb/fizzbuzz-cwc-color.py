# https://pypi.org/project/termcolor/
# pip3 install termcolor --user

import sys, time
from termcolor import colored

def main():
	print (colored('FizzBuzz', 'red'))
	time.sleep(2)
	for n in range(1,101):
		if n % 3 == 0:
			print("\t\t",end="")
			print("Fizz",end="")
		if n%5 != 0:
			print()
		if n % 5 == 0:
			print("Buzz")
		if n % 3 != 0 and n % 5 != 0:
			print(n)
		if(n % 10 == 0):
			time.sleep(2)

if __name__ == '__main__':
	main()
