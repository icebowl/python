import random
key = ["","","","",""]
code = ["","","","",""]
codevalues = [-1,-1,-1,-1,-1]
#print colors
print("CHATBOT PYTHON - CWC")
print("ASC2 TABLE CHARACTERS 33 TO 126",end="")

#print asc2 table 33 to 126
for i in range (33,127):
    c = chr(i)
    print(str(i)+"="+str(c)+" ",end="")
    if (i % 10 == 0):
        print()
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
print("HERE IS THE CODE MATRIX")
for j in range (0,5):
    print(key[j])
    keyvalue = random.randint(0,7)
    temp = key[j]
    temp = temp[codevalues[j]]
    code[j] = temp
#print(code) debuf
print("TYPE THE CHARACTER CODE THEN PRESS Enter . . .")
check = 0
i = 0
row = input("ROW "+str(i+1)+" COLUMN "+str(codevalues[i]+1)+" CHARACTER.")
if (row == str(code[i])):
	check = check + 1
elif (row == "**"):
	print(" 42 ! ")
else:
	print("* NOT 42 *");
i = 1
row = input("ROW "+str(i+1)+" COLUMN "+str(codevalues[i]+1)+" CHARACTER.")
if (row == str(code[i])):
	check = check + 1
elif (row == "**"):
	print(" 42 ! ")
else:
	print("* NOT 42 *");
i = 2
row = input("ROW "+str(i+1)+" COLUMN "+str(codevalues[i]+1)+" CHARACTER.")
if (row == str(code[i])):
	check = check + 1
i = 3
row = input("ROW "+str(i+1)+" COLUMN "+str(codevalues[i]+1)+" CHARACTER.")
if (row == str(code[i])):
	check = check + 1
i = 4
row = input("ROW "+str(i+1)+" COLUMN "+str(codevalues[i]+1)+" CHARACTER.")
if (row == str(code[i])):
	check = check + 1
if(check == 5):
    print("\n\n")
    print("YOU ARE NOT A ROBOT!")
    print("\n\n")
else:
    print("\n\n")
    print("ROBOT DETECTED!")
    print("\n\n")
print("\n")

