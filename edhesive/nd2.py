n = int(input("Numerator : " ))
d = int(input("Denominator : "))
f = 0
if (d == 0):
 print("Error - cannot divide by zero.")
else:
 if (n >= 0  and n < 65535 and d >=0 and d < 65535):
  f = float(n/d);
 else:
  print("LARGE NUMBER")
print ("Decimal: "+str(f))

