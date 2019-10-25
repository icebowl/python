'''
sudo apt install python-pip;
sudo apt install python3-pip;
pip install colorama;
python3 -m pip install colorama;

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
print(Fore.CYAN+"CHATBOT PYTHON - CWC")
print(Fore.CYAN+"ASC2 TABLE CHARACTERS 33 TO 126",end="")
print(Style.RESET_ALL,end="")

#print asc2 table 33 to 126  cwc
print(Fore.BLACK,end="")
print(Back.YELLOW)
#print asc2 table 33 to 126
for i in range (33,127):
    c = chr(i)
    print(str(i)+"="+str(c)+" ",end="")
    if (i % 10 == 0):
        print()
print(Style.RESET_ALL)
# create random code values
for j in range (0,5):
    codevalues[j] = random.randint(0,7)
#print(codevalues) debug
#create code table
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
#get codes
print(Back.BLUE,end="")
print(Fore.BLACK+"CODE MATRIX")
print(Style.RESET_ALL,end="")
print(Back.WHITE,end="")
print(Fore.BLUE,end="")
for j in range (0,5):
    print(key[j])
    keyvalue = random.randint(0,7)
    temp = key[j]
    temp = temp[codevalues[j]]
    code[j] = temp
#print(code) debuf
print(Back.BLUE,end="")
print(Fore.BLACK+"Type the CHARACTER from the CODE MATRIX ")
print(Fore.BLACK+"then press Enter . . .")
print(Style.RESET_ALL)
check = 0
for i in range (0,5):
    row = input("ROW "+str(i+1)+" COLUMN "+str(codevalues[i]+1)+" CHARACTER : ")
    if (row == str(code[i])):
        check = check + 1
if(check == 5):
    print(Fore.BLACK,end="")
    print("\n\n")
    print(Back.GREEN+"YOU ARE NOT A ROBOT!")
    print("\n\n")
else:
    print(Fore.BLACK,end="")
    print("\n\n")
    print(Back.RED+"ROBOT DETECTED!")
    print("\n\n")
print(Style.RESET_ALL)
print("\n")
