# save file as "binary-demo.py" cwc
def binstring():
    for n in range (0,256):
        b1 = bin(n)
        b2 =  b1.replace("0b", "")
        print(n,b2,end="")
        blength = len(b2)
        print(" ",blength)

def main():
    binstring()

main()
