#!/usr/bin/python
import sys
import binascii

def bincon(n):
 print("bincon ",n)


def main():
 print (len(sys.argv))
 print (str(sys.argv))
 s = sys.argv[1]
 n = len(s)
 bincon(s)
 print(s,n)

main()

