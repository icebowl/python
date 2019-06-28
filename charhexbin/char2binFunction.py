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
  #barray[0] = b
  #end loop

def main():
 print (len(sys.argv))
 print (str(sys.argv))
 word = sys.argv[1]
 n = len(word)
 bincon(word)
 print("main ",word,n)

main()

