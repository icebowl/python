from datetime import datetime
now =datetime.now()

print('%s/%s/%s' %(now.month,now.day,now.year))
print('%s:%s:%s' %(now.hour,now.minute,now.second))
yearString = str(now.year)
print('YEAR %s'%now.year)
print (yearString[2:4]+'%s' %now.hour)
