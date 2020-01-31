from datetime import datetime
now =datetime.now()

#print('%s/%s/%s' %(now.month,now.day,now.year))
#print('%s:%s:%s' %(now.hour,now.minute,now.second))
nowYear = str(now.year)
nowSeconds = str(now.second)
dateTimeString =  nowYear[2:4]+str(now.month)+str(now.day)+"-"+str(now.hour)+"-"+str(now.minute)+"-"+nowSeconds[0:2]
print(dateTimeString)
