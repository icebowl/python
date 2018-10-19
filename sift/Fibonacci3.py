# Fibonacci sequence:
# cwcoleman
a = 1
b = 0
f = 0
c = 0 # this is the counter
print()
while c < 20:
   print(f, end=" ")
   f = a + b
   a = b
   b = f
   c = c + 1
print()

# a  |  b  | f
# -  |  -  | -
#    |     | 0
# 1  |  0  | 1
# 0  |  1  | 1
# 1  |  1  | 2
# 1  |  2  | 3
# 2  |  3  | 5
# 2  |  3  | 5
# 2  |  3  | 5
# 2  |  3  | 5
# 2  |  3  | 5
