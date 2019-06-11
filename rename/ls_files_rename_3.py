import os, sys
print(sys.argv)
path = '.'
filelist = []
files = os.listdir(path)

for i in range(0,len(filelist)):
    #print("mv \""+filelist[i]+"\" wooten2018-"+str(i)+".jpg;")
	print(filelist[i])

