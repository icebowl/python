#!/usr/bin/env python3
import math
def isprime(n):
   if n <= 1:
      return False
   else:
      # iterating loop till square root of n
      for i in range(2, int(math.sqrt(n)) + 1):
         # checking for factor
         if n % i == 0:
            # return False
            return False
      # returning True
      return True

def main():
	for n in range (1,32):
		ip = isprime(n)
		print(n,ip)
if __name__ == "__main__":
	main()
