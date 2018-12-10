# save file as "string-demo.py" cwc
from time import sleep
def string_methods():
    a = "Hello World!"
    b = "Hello, World!"
    s = 1
    print(a[0])
    sleep(s)
    print(a[1])
    sleep(s)
    print(b[2:5])
    sleep(s)
    print("a.strip()")
    print(a.strip())
    sleep(s)
    print(len(a))
    sleep(s)
    print(a.lower())
    sleep(s)
    print(a.replace("H", "J"))
    sleep(s)
    print(b.split(",")) # returns ['Hello', ' World!']

def binstring():
    b1 = bin(7)
    b2 =  b1.replace("0b", "")
    print("bin 7 ",b1,b2)

def main():
    string_methods()
    binstring()
    print("Enter a binary number:",end="")
    bn = input()
    print("binary: " + bn)
main()
