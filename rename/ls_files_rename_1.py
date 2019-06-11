import os, sys
print(sys.argv)
path = '.'
filelist = []
files = os.listdir(path)
for name in files:
    if (name != sys.argv[0]):
        filelist.append(name)

for i in range(0,len(filelist)):
    print(filelist[i])

#wooten2017-5.jpg
