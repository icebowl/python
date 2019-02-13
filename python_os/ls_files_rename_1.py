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


for i in range(0,len(filelist)):
    print("mv \""+filelist[i]+"\" wooten2018-"+str(i)+".jpg;")

#wooten2017-5.jpg
