#cwc reset control+j
# https://www.youtube.com/watch?v=BK7YvpTT4Sw
import time
import curses
import random

def main(stdscr):
	hscore = 0;cscore = 0;randomKeep = 0
	curses.curs_set(0)
	stdscr.addstr(2,11,"PIG BY CWC - NO WARRANTY - TYPE (reset then control+j) IF tty  CRASHES")
	stdscr.addstr(3,13,"LET'S GET STARTED")
	stdscr.addstr(4,13,"TYPE K OR k to KEEP YOUR SCORE")
	stdscr.addstr(5,13,"TYPE ANY OTHER KEY TO ROLL")
	stdscr.addstr(6,13,"TYPE Q or q to TO QUIT")
	stdscr.refresh()
	while (hscore < 100 and cscore < 100):
		count = 1
		keep = "*"
		done = 0
		scoreTemp = 0
		#human 
		while (done == 0):
			roll = 0
			player = "HUMAN"
			stdscr.addstr(14,17,"                                                                                                                        ")
			stdscr.addstr(14,17,"SCORES -> HUMAN= "+str(hscore)+" COMPUTER= "+str(cscore)+" CURRENT TURN SCORE= "+str(scoreTemp))
			#stdscr.addstr(16,17,"-----------------------------------------------------------------------------------------------")
			stdscr.addstr(16,17,"-----------------------------------------------------------------------------------------------")
			stdscr.addstr(16,17,"THE - "+ player+" - IS THE PLAYER.")
			#k = stdscr.get_wch()
			k = stdscr.getkey()   
			keep =  k[0].lower()
			#stdscr.addstr(30,10,"keep variable debug"+str(keep))
			curses.flushinp()
			if (keep == 'k'):
				hscore = hscore + scoreTemp
				scoreTemp = 0
				done = 1
			roll = random.randint(1,6)
			stdscr.addstr(18,17,"ROLL NUMBER "+str(count)+" THE CURRENT ROLL IS "+str(roll))
			count = count + 1
			if (roll != 1):
				scoreTemp = scoreTemp + roll
			else:
				scoreTemp = 0
				done = 1
			# * * * * * * * * * * * * * * * * * * * * * * *
				#computer
		done = 0
		scoreTemp = 0
		while (done == 0):
			player = "COMPUTER"
			stdscr.addstr(14,17,"                                                                                                                        ")
			stdscr.addstr(14,17,"SCORES -> HUMAN= "+str(hscore)+" COMPUTER= "+str(cscore)+" CURRENT TURN SCORE= "+str(scoreTemp))
			stdscr.addstr(16,17,"*************************************************************************************************************************")
			stdscr.addstr(16,57,"THE - "+ player+" - IS THE PLAYER.")
			keep = chr(random.randint(0,5)+107)
			stdscr.addstr(0,40,"COMPUTE KEEP KEY "+keep)
			if (keep == 'k'):
				cscore = cscore + scoreTemp
				scoreTemp = 0
				done = 1
			roll = random.randint(1,6)
			stdscr.addstr(18,57,"ROLL NUMBER "+str(count)+" THE CURRENT ROLL IS "+str(roll))
			count = count + 1
			if (roll != 1):
				scoreTemp = scoreTemp + roll
			else:
				scoreTemp = 0
				done = 1
			#time.sleep(3)
	stdscr.addstr(2,11,"                                                                      ")
	stdscr.addstr(3,13,"                                                                      ")
	stdscr.addstr(4,13,"                                                                      ")
	stdscr.addstr(5,13,"                                                                      ")
	stdscr.addstr(6,13,"                                                                      ")
	stdscr.addstr(7,13,"* * * * * * * FINAL SCORE * * * * * * *")
	stdscr.addstr(8,13,"SCORES -> HUMAN= "+str(hscore)+" COMPUTER= "+str(cscore))
	time.sleep(3)
			
			
			#while True:
			#	k = stdscr.get_wch()
			#	keep =  k[0].lower()
			#	curses.flushinp()
			#	if (keep == 'k'):
			#		stdscr.addstr(11,5," KEEP ")
			#	if( k == "q"):
			#		False
	
	#time.sleep(3)
	
curses.wrapper(main)

'''
from colorama import Fore, Back, Style 
print(Fore.RED + 'THE PIG GAME') 
print(Style.RESET_ALL) 



import sys
hscore = 0
cscore = 0
randomKeep = 0

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
