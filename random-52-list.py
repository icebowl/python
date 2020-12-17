#python3 random-52-list.py cwc
# This code simulates shuffling a deck of 52 card.
# nlist is a list of integers 0 to 51 sorted
# zlist is a list filled with negative ones (-1)
# What I've done is randomly generate an integer from 0 to 51
# then decicde if it is take if from the nlist and move it to the z list
# in another location based on the random number is taken.
# Once a number is taken fro nlist a -1 put in it's place.
# 
import random
			
def main():
	nlist = [0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,
             21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,
             41,42,43,44,45,46,47,48,49,50,51,51] 
             
	zlist =[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,
			-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,
			-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1-1,-1]
	# start of shuffle		
	count = 0
	totalrandom = 1
	while (count < 52):
		done = 0 # 0 is false
		while (done == 0):
			n =  random.randint(0,51)
			totalrandom = totalrandom + 1
			#print(" n:", n,end="")
			if (nlist[n] == -1):
				done = 0
			else:
				zlist[count] = n
				nlist[n] = -1
				count = count + 1
				done = 1
	print(" nlist *****")
	print(nlist)
	print(" zlist *****")
	print(zlist)
	print("Total Random ",totalrandom)

	
main()
