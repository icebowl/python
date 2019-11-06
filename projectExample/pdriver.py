import turtle
import one
import two 
import three

def main():
	done = 0
	while (done == 0):
		one.main()
		two.main()
		three.main()
		q = input(" * ")
		if (q == "1"):
			done = 1

if __name__ == '__main__':
	main()
	
