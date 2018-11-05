import os, sys
print(sys.argv)
path = '.'
filelist = []
files = os.listdir(path)
for name in files:
    #print(name)
    #if (name != "list1.py"):
    if (name != sys.argv[0]):
        filelist.append(name)

for i in range(0,len(filelist)):
    print(filelist[i])

filelist.sort()
for i in range(0,len(filelist)):
    print("mv \""+filelist[i]+"\" filea"+str(i)+".png;")
