#!/usr/bin/python
import sys
import binascii

print (len(sys.argv))
print (str(sys.argv))
s = sys.argv[1]
n = len(s)
print(s,n)
clean = []
for i in range(n):
 #print (hex(ord(s[i])),' ',end='')
 clean = hex(ord(s[i]))[2:4]
 print(clean,' ',end='')

print()
'''
print binascii.b2a_hex("hello world")

'''
