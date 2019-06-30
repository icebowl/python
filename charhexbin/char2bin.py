#!/usr/bin/python
import sys
import binascii
def binary(c):
 temp =""
 bstring = ""
 c1 = ord(c)
 dividend = 128
 #print("The character ",c1)
 for n in range(0,8):
  temp = str(c1 % 2)
  c1 = int(c1 / 2) 
  bstring = bstring + temp
 bstring = bstring[::-1] # reverse order of string
 return bstring

def bincon(word):
 c = ""
 b = ""
 n = len(word)
 temp = word
 print("n ",n,"\n\n")
 for i in range(0,n):
  #print (word[i:i+1]," ",end="")
  c = word[i:i+1]
  bc = binary(c)
  #print("c ",c," ",bc)
  print(bc,end="") 
  '''
  b =bin(ord(word[i:i+1]))
  print (word[i:i+1]," ",end="")
  temp = str(b)
  print(temp)
  temp = temp[2:1]
  print(temp,temp[2:])
  #end loop
'''
def main():
 print (len(sys.argv))
 print (str(sys.argv))
 word = sys.argv[1]
 n = len(word)
 bincon(word)
 print(" THE WORD IS ",word,n)

main()

