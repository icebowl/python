import random
hscore = 0
cscore = 0
randomKeep = 0
toggle_hc = -1 # human is -1
scoreTemp = 0
print("LET'S GET STARTED")
print("TYPE K OR k to KEEP YOUR SCORE")
print("TYPE ANY OTHER CHARACTER TO ROLL")
while (hscore <= 100 or cscore <= 100):
	roll = 0
	keep = "k"
	#roll the numbers
	while (roll !=1 and keep =="k"):
		if (toggle_hc == -1):
			player = " - HUMAN - "
		else:
			player =" - COMPUTER - "
		print(player+" IS THE PLAYER.")
		print("SCORES HUMAN",hscore," COMPUTER ",cscore)
		if (toggle_hc == 1):
			keep = chr(random.randint(0,1)+107)
			print("COMPUTE KEEP KEY "+keep)
			temp = input("THIS IS A DEBUG")
		else:
			keepTheScore = input("Keep your total score? (type \'k\' to keep) ")
			keep =  keepTheScore[0].lower()
		if (keep == 'k'):
			toggle_hc = toggle_hc * -1
		print ("keep",keep)
		roll = random.randint(1,6)
		print("* * * *\nROLL",roll,"\n* * *  *")
		scoreTemp = scoreTemp + roll
		if (roll == 1):
			if(toggle_hc == -1):
				hscore = -1
			else:
				cscore = -1
		if (toggle_hc == -1):
			hscore = hscore + roll
		else:
			cscore = cscore = roll
		
'''



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




import random
playerScore = 0
compScore = 0
while (playerScore < 100 and compScore < 100):
    roll = 2
    again = "B"
    #Player's Turn   
    pTurnTotal = 0
    while (roll != 1 and again == "B"):
        roll = random.randint(1,6)
        #print (roll)
        if (roll != 1):
             pTurnTotal = pTurnTotal + roll
             message = "You rolled a " + str(roll) + "\n\nEnter A to hold and B to roll again\n\nYour turn score is: "
             message = message + str(pTurnTotal) + "\nYour Score is: " + str(playerScore)
             message = message + "     Computer Score: " + str(compScore)
             again = input(message)
        if (again == "A"):
             playerScore = playerScore + pTurnTotal
             pTurnTotal = 0
    #Computer's Turn
    cTurnTotal = 0
    compAgain = 2
    roll = 9
    while (roll != 1 and compAgain == 2):
        roll = random.randint(1,6)
        print("Computer rolled: " + str (roll))
        if (roll != 1):
           cTurnTotal = cTurnTotal + roll
           compAgain = random.randint(1,2)
        if (compAgain == 1):
            compScore = compScore + cTurnTotal
            cTurnTotal = 0
            print ("Computer ends turn.")
        else:
            print ("Computer rolls again.")
print ("Computer Score: " + str(compScore))
print ("Player Score: " + str(playerScore))
'''
    

