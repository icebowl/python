a = [[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]]
print(a,"\n")
for x in range(0,2):
    for y in range (0,2):
        for z in range (0,3):
            print("x=",x,"|",end="")
            print (a[x][y][z]," ",end="")
        print()
print()
print(" ~~~~~~~~~~~~~~~~~~~ ")
print(a[0][0][0])
print(a[0][1][0])
print(a[0][1][1])
print(a[0][1][2])
print(a[0][1][2])
print(a[1][1][2])
print(a[0])
