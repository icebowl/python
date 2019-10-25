'''
colorama 
Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
Style: DIM, NORMAL, BRIGHT, RESET_ALL
print(Fore.RED + 'some red text')
print(Back.GREEN + 'and with a green background')
print(Style.DIM + 'and in dim text')
print(Style.RESET_ALL)
print('back to normal now')

'''
from colorama import Fore, Back, Style
import random
key = ["","","","",""]
code = ["","","","",""]
codevalues = [-1,-1,-1,-1,-1]
#print colors
print(Fore.CYAN+"CHATBOT PYTHON - CWC",end="")
print(Style.RESET_ALL,end="")
#print asc2 table 33 to 126  cwc
print(Fore.BLACK,end="")
print(Back.YELLOW,end="")
for i in range (33,127):
    c = chr(i)
    print(str(i)+"="+str(c)+" ",end="")
    if (i % 10 == 0):
        print()
print(Style.RESET_ALL)
for j in range (0,5):
    codevalues[j] = random.randint(0,7)
print(codevalues)
#create 
for j in range (0,5):
    s = ""
    k = 0
    while (k < 8):
        v = 0
        v = random.randint(33,126)
        if (v !=47 and v !=92):
            c = chr(v)
            s = s + c
            k = k + 1
            #print("k ",k)
    key[j] = s
for j in range (0,5):
    print(key[j])
    keyvalue = random.randint(0,7)
    temp = key[j]
    temp = temp[codevalues[j]]
    code[j] = temp
print("\n\n")
print(code)


