from random import randint

while True:
	txt = randint(30,37)
	bck = randint(40,47)
	print("\033[1;{0};{1}m" "_______{0}_______{1}_______".format(txt,bck))
	for i in range(10000000):
		pass
	
