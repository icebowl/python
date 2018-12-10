# save file as "string-demo.py" cwc
from time import sleep
def string_methods():
    a = "Hello World!"
    b = "Hello, World!"
    c = "     Hello, World!"
    s = 1
    print("--- a sub 0 ---")
    print(a[0])
    sleep(s)
    print("--- a sub 1 ---")
    print(a[1])
    sleep(s)
    print("--- a sub 2 to 5 ---")
    print(b[2:5])
    sleep(s)
    print("--- c.strip  white space ---")
    print(c)
    print("c.strip()")
    print(c.strip())
    sleep(s)
    print("--- length of a string ---")
    print(len(a))
    sleep(s)
    print("--- convert to lower ---")
    print(a.lower())
    sleep(s)
    print("--- replace H with J ---")
    print(a.replace("H", "J"))
    sleep(s)
    print("--- split b into a list opf 2 strings ---")
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
