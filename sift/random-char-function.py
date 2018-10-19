import random
def randomint():
	random_number = random.randint(33,200)
	random_character = chr(random_number)
	return random_character

def main():
	for i in range(100):
		rchar =  randomint();
		if (rchar == "A"):
			print("\033[1;32;40m",rchar,end="")
		else:
			print("\033[1;34;40m",rchar,end="")

main()
#grep -o '67' 65536-integers.txt | wc -l
# print("\033[1;32;40m Bright Green   \033[0m 1;32;40m            \033[0;32;47m Green      \033[0m 0;32;47m               \033[0;37;43m Black      \033[0m 0;37;43m")
