# save file as "string-demo.py" cwc
from time import sleep
def string_methods():
    a = "Hello World!"
    b = "Hello, World!"
    c = "     Hello, World!"
    s = 1
    print(a[0])
    sleep(s)
    print(a[1])
    sleep(s)
    print(b[2:5])
    sleep(s)
    print(c)
    print("c.strip()")
    print(c.strip())
    sleep(s)
    print(len(a))
    sleep(s)
    print(a.lower())
    sleep(s)
    print(a.replace("H", "J"))
    sleep(s)
    print("split(\",\")")
    d = b.split(",")
    print(d)
    print(d[0])
    print(d[1])
def main():
    string_methods()
    print("Enter a binary number:",end="")
    bn = input()
    print("binary: " + bn)

main()
