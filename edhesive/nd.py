done = False
while(done == False):
 n = int(input("Numerator : " ))
 d = int(input("Denominator : "))
 if (n >= 0 and n < 65521 and d >=0 and d < 65521):
  done = True

if (d == 0):
   print("Error - cannot divide by zero.")
else:
   f = float(n/d);      ####  The mistake is right here on this line ####
   print ("Decimal: "+str(f))

