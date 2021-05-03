#useradd -m -d /home/users/zoey zoey -s /bin/bash;
#echo "zoey:password" | chpasswd


def string_concat_users(a):
    b = "useradd -m -d /z/users/"+a[0]+" "+a[0]+" -s /bin/bash;"
    #zoey -s /bin/bash;"
    #b = b + a
    #b = b +"?tab=repositories\" target =\"_blank\" >"+a+"</a><br />"
    # b = b +"?tab=repositories\" target ="+ '"'+"_blank"+'"'+">"+a+"</a><br />"
    return b

def string_concat_passwords(a):
    b = "echo \""+a[0]+" "+a[1]
    return b

def main():
		users = [['user1','abc123'],
	['user2','asd432'],
	['user3','spa124'],
	['daniel'],['pwd'],
['drew'],['pwd'],
['austin'],['pwd'],
['ian'],['pwd'],
['anisha'],['pwd'],
['marc'],['pwd'],
['gavin'],['pwd'],
['osvaldo'],['pwd'],
['tyler'],['pwd'],
['shawn'],['pwd'],
['axel'],['pwd'],
['juan'],['pwd'],
['ulises'],['pwd'],
['logan'],['pwd'],
['btj'],['pwd'],
['preston'],['pwd'],
['alejandro'],['pwd'],
['noor'],['pwd'],
['gerardo'],['pwd'],
['andrew'],['pwd'],
['cian'],['pwd'],
['caleb'],['pwd'],
['adam'],['pwd'],
['taj'],['pwd'],
['levi'],['pwd'],
['seth'],['pwd'],
['ian'],['pwd']
]
	for n in range (0,len(users)):
		a = users[n]
		b = string_concat_users(a)
		print(b)

	print("\n\n * * * * * * * * \n\n")
	for n in range (0,len(users)):
		a = users[n]
		b = string_concat_passwords(a)
		print(b)

if __name__ == '__main__':
    main()

'''


def string_concat_repos(a):
	b = "<a href = "+'"'+"https://github.com/"
	b = b + str(a[1])
	b = b +"?tab=repositories\" target =\"_blank\" >"+a[0]+"-"+a[1]+"</a><br />"
	return b

def string_concat_io(a):
    b = "<a href = "+'"'+"https://"
    b = b + a + ".github.io"
    b = b +'"' + " target ="+ '"'+"_blank"+'"'+">"+a[0]+"</a><br />"
    return b

def main():
	users = [['A,Ulises','ulises-aguilar']
,	['A,Miguel A','MiguelAlcalan2020']
,	['B,Christopher Logan','Logan-Benner']
,	['B,Daniel S','danielbrogan26']
,	['D,Andrew','DemonDrew0508']
	]
	for n in range (0,len(users)):
		a = users[n]
		#b = string_concat_io(a)
		print(a)

	print("\n\n * * * * * * * * \n\n")
	for n in range (0,len(users)):
		a = users[n]
		b = string_concat_repos(a)
		print(b)

if __name__ == '__main__':
    main()

'''
