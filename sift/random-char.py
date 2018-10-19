import random
for i in range(1000000):
	random_number = random.randint(65,91)
	random_character = chr(random_number)
	if (random_number == 65):
		print("\033[1;32;40m",random_character,end="")
	else:
		print("\033[1;34;40m",random_character,end="")


#print(random_number, random_character)
#grep -o '67' 65536-integers.txt | wc -l
# print("\033[1;32;40m Bright Green   \033[0m 1;32;40m            \033[0;32;47m Green      \033[0m 0;32;47m               \033[0;37;43m Black      \033[0m 0;37;43m")
