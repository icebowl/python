# save file as "binary-demo.py" cwc
def binstring():
    for n in range (0,256):
        b1 = bin(n)
        b2 =  b1.replace("0b", "")
        print(n,b2,end="")
        blength = len(b2)
        #print(" ",blength)
        if blength == 1:
            b2 = "0000000"+b2
        elif blength == 2:
            b2 = "000000"+b2
        elif blength == 3:
            b2 = "00000"+b2
        elif blength == 4:
            b2 = "0000"+b2
        elif blength == 5:
            b2 = "000"+b2
        elif blength == 6:
            b2 = "00"+b2
        elif blength == 7:
            b2 = "0"+b2
        print(" ",b2,blength)

def main():
    binstring()

main()
