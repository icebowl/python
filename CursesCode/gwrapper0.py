#cwc reset control+j
# https://www.youtube.com/watch?v=BK7YvpTT4Sw
import time
import curses

def main(stdscr):
	curses.curs_set(0)
	stdscr.addstr(15,5," 15 5 ")
	stdscr.refresh()
	while True:
		k = stdscr.get_wch()
		print(f'k: {k}')
		curses.flushinp()
		if (k == 'k'):
			stdscr.addstr(20,5," k 20 5 ")
		if( k == "q"):
			False
	
	#time.sleep(3)
	
curses.wrapper(main)

'''
'''
sudo apt install python-pip
sudo apt install python3-pip
pip install colorama
python3 -m pip install colorama
'''
from colorama import Fore, Back, Style 
print(Fore.RED + 'THE PIG GAME') 
print(Style.RESET_ALL) 


import random
import sys
hscore = 0
cscore = 0
randomKeep = 0
print("LET'S GET STARTED")
print("TYPE K OR k to KEEP YOUR SCORE")
print("TYPE ANY OTHER CHARACTER TO ROLL")
print("THEN PRESS THE \'Enter\' KEY\n\n")
while (hscore <= 100 and cscore <= 100):
	#roll = 0
	count = 1
	keep = "*"
	done = 0
	scoreTemp = 0
	#human 
	while (done == 0):
		roll = 0
		player = "HUMAN"
		print("THE - "+ player+" - IS THE PLAYER.")
		print("SCORES -> HUMAN= ",hscore," COMPUTER= ",cscore," CURRENT TURN SCORE= " , scoreTemp)
		keepTheScore = input("Keep your total score? ( type \'k\' to keep ) ")
		keep =  keepTheScore[0].lower()
		if (keep == 'k'):
			hscore = hscore + scoreTemp
			scoreTemp = 0
			done = 1
		roll = random.randint(1,6)
		print("\nROLL NUMBER "+str(count)+" THE CURRENT ROLL IS ",roll,"\n\n")
		count = count + 1
		if (roll != 1):
			scoreTemp = scoreTemp + roll
		else:
			scoreTemp = 0
			done = 1
	#computer
	done = 0
	while (done == 0):
		print(Fore.RED + 'COMPUTER') 
		player = "COMPUTER"
		print("\t\t\tTHE - "+ player+" - IS THE PLAYER.")
		print("\t\t\tSCORES -> HUMAN= ",hscore," COMPUTER= ",cscore," CURRENT TURN SCORE= " , scoreTemp)
		keep = chr(random.randint(0,5)+107)
		print("\t\t\tCOMPUTE KEEP KEY "+keep)
		#temp = input("THIS IS A DEBUG ")
		if (keep == 'k'):
			cscore = cscore + scoreTemp
			scoreTemp = 0
			done = 1
			print(Style.RESET_ALL)	
		roll = random.randint(1,6)
		print("\n\t\t\tiROLL NUMBER "+str(count)+" THE CURRENT ROLL IS ",roll,"\n\n")
		count = count + 1
		if (roll != 1):
			scoreTemp = scoreTemp + roll
		else:
			scoreTemp = 0
			done = 1
			print(Style.RESET_ALL)	
print("FINAL SCORE ")
print("SCORES -> HUMAN= "+str(hscore)+" COMPUTER= "+str(cscore))
'''

elif (toggle_hc == 1):
			keep = chr(random.randint(0,5)+107)
			print("COMPUTE KEEP KEY "+keep)
			temp = input("THIS IS A DEBUG")
			if (keep == 'k'):
				print("\t\tCOMPUTER IS GOING TO KEEP THE SCORE.")
				#toggle_hc = toggle_hc * -1
				cscore = cscore + scoreTemp
				scoreTemp = 0
Play Pig

The game Pig was invented in 1945 by John Scarne. 
It is a simple dice game played by two people.

The rules for Pig are simple.
 Players Roll one die and keep track of their points per turn using the following rules:

    Roll any other number but one you add it to your turn total and keep rolling until you roll a 1.
    If you roll a 1, no score and it becomes the next player's turn. Basically you lose your turn total points.
    The player can choose to hold. This means their turn total is added to their score and it becomes the next player's turn.
    The first person to score 100 or above wins.

Write a program to allow a user to play Pig against the computer. 
The computer's rolls and choices should be created using random numbers. 
The player's rolls should be created using random numbers, and they should be asked if they want to hold or roll.

The player should go first.


'''
    





'''
