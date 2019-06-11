import os
path = '/home/cwc/http/wooten/photos/wootenphotos2018/'
filelist = os.listdir(path)
filelist.sort()
trimmed = list()
for i in range (0,len(filelist)):
	temp = "wooten2018-"+str(i+1)+".jpg;"
	trimmed.append(temp)

for i in range (0,len(filelist)):
	print ("mv ", filelist[i],"thumb-"+str(filelist[i]))




"""

<li>	<a href="#">	<img src="images/thumbs/thumb-wooten2017-1.jpg" data-large="images/wooten2017-1.jpg" data-description="2017 # 1" />	</a>	</li>

>>> x = "Hello World!"
>>> x[2:]
'llo World!'
>>> x[:2]
'He'
>>> x[:-2]
'Hello Worl'
>>> x[-2:]
'd!'
>>> x[2:-2]
'llo Worl'





"""
