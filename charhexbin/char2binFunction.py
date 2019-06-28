#!/usr/bin/python
import sys
import binascii

def bincon(word):
 c = ""
 b = ""
 n = len(word)
 print("n ",n,"\n\n")
 for i in range(0,n):
  b =bin(ord(word[i:i+1]))
  print (word[i:i+1]," ",b)
 #end loop
 print("bincon ",word)
 c1 = word[0:1]
 c2 = word[1:2]
 
 print("c ",c1,c2)

def main():
 print (len(sys.argv))
 print (str(sys.argv))
 word = sys.argv[1]
 n = len(word)
 bincon(word)
 print("main ",word,n)

main()

