from random import randint
def randlist(r):
	alpha = ["abcdefghijklmnopqrstuvwxyz", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "01234567890",]
	abcdefghijklmnopqrstuvwxyz = alpha[r]
	return abcdefghijklmnopqrstuvwxyz

def main():
	done = False
	while done == False:
		r = randint(0,5)
		abcdefghijklmnopqrstuvwxyz = randlist(r)
		print(alpha,end=" ")
main()

