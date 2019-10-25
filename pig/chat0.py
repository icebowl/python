import random
key = ["","","","",""]
code = ["","","","",""]
codevalues = [-1,-1,-1,-1,-1]

#asc2.py cwc
for i in range (33,127):
    c = chr(i)
    print(str(i)+"="+str(c)+" ",end="")
    if (i % 10 == 0):
        print()

for j in range (0,5):
    codevalues[j] = random.randint(0,7)
print(codevalues)
for j in range (0,5):
    s = ""
    for k in range (0,8):
        v = 0
        while(v != 47):
            v = random.randint(33,126)
            print(" v ",v," ")
            c = chr(v)
        #print(c)
        s = s + c
    key[j] = s
    #print(s)

for j in range (0,5):
    print(key[j])
    keyvalue = random.randint(0,7)
    temp = key[j]
    temp = temp[codevalues[j]]
    code[j] = temp
print("\n\n")
print(code)

