# list123.py
# No functions. Just code.
1dlist = [1,2,3,4,5,6,7,8,9,10,11,12]
print("1 DIMENSIONAL LIST")
print (1dlist)

2dlist = [[1,2,3,4,5,6,7,8,9,10,11,12],
    [13,14,15,16,17,18,19,20,21,22,23,24],
    [25,26,27,28,29,30,31,32,33,34,35,36]]
print(a,"\n\n")
for r in range(0,3):
    for c in range (0,12):
        print (2dlist[r][c]," ",end="")
    print()
print()
print(a[0][0])
print(a[1][0])
print(a[2][0])


3dlist = [[[1,2,3],[4,5,6],[7,8,9]],
        [[10,11,12],[13,14,15],[16,17,18]],
        [19,20,21],[22,23,24],[25,26,27]]]
print(a,"\n")
for x in range(0,3):
    for y in range (0,3):
        for z in range (0,3):
            print (3dlist[x][y][z]," ",end="")
        print()
print()
print(" ~~~~~~~~~~~~~~~~~~~ ")
print(a[0][0][0])
print(a[1][0][0])
print(a[0][1][0])
