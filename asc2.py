#asc2.py cwc
for i in range (0,100):
    c = chr(i)
    print("[",i,"=",c,"]",end="")
    if (i % 10 == 0):
        print("\n")
