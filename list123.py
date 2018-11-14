# list123.py
# No functions. Just code.
# Look at the square brackets []  [[]] [[[]]]

print("* * * * * * * * * * * * * *")
print("1 DIMENSIONAL LIST")
oneD = [1,2,3,4,5,6,7,8,9,10,11,12]
print (oneD)
for n in range (0,len(oneD)):
    print (oneD[n]," ", end="")

print()
print("* * * * * * * * * * * * * *")
print("2 DIMENSIONAL LIST")
twoD = [[1,2,3,4,5,6,7,8,9,10,11,12],
    [13,14,15,16,17,18,19,20,21,22,23,24],
    [25,26,27,28,29,30,31,32,33,34,35,36]]
print(twoD,"\n\n")
for r in range(0,3):
    for c in range (0,12):
        print (twoD[r][c]," ",end="")
    print()
print()
print(twoD[0][0])
print(twoD[1][0])
print(twoD[2][0])

print("* * * * * * * * * * * * * *")
print("3 DIMENSIONAL LIST")
threeD = [[[1,2,3],[4,5,6],[7,8,9]],
        [[10,11,12],[13,14,15],[16,17,18]],
        [[19,20,21],[22,23,24],[25,26,27]]]

print(threeD,"\n")
for x in range(0,3):
    for y in range (0,3):
        for z in range (0,3):
            print (threeD[x][y][z]," ",end="")
        print()
print()
print(threeD[0][0][0])
print(threeD[1][0][0])
print(threeD[0][1][0])
