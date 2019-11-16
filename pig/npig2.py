#cwc
import random
#globals
t = "@\t"
def display(roll,tempscore,player,hcount,ccount,h,c):
    trow = "* * * * * * * * * * * * * * * * * * * * * * * * *\n*\tTYPE K TO KEEP ANY OTHER KEY TO ROLL "
    if(player == -1):
        t="*\t"
        playerName = "HUMAN"
    else:
        t= "*\t\t\t\t"
        playerName = "COMPUTER"
    #print(t+"roll  count  h  c")
    print(trow)
    print(t+"PLAYER "+playerName)
    print(t+"ROLL VALUE "+str(roll)+" CURRENT ROLL SCORE "+str(tempscore))
    print(t+"HUMAN TOTAL "+str(h)+" COMPUTER TOTAL "+str(c))
    print(trow)

def main():
    h = 0;c = 0; tempscore = 0; player = -1
    print("LET'S GET STARTED")
    print("TYPE K OR k to KEEP YOUR SCORE")
    print("TYPE ANY OTHER CHARACTER TO ROLL")
    print("THEN PRESS THE \'Enter\' KEY")
    print("JUST TYPING \'Enter\' WILL CRASH THE GAME.\n")
    hcount = 0;ccount = 0
    while (h < 100 and c < 100):
        keep = "*"
        roll = random.randint(1,6)
        display(roll,tempscore,player,hcount,ccount,h,c)
        if (roll == 1):
            tempscore = 0
            player = player * -1
        elif(player == -1):
            keepTheScore = input ("Keep the score ? ")
            keep =  keepTheScore[0].lower()
            if (keep == 'k'):
                h= h + tempscore + roll
                player = player * -1
            else:
                tempscore = tempscore + roll
                hcount = hcount + 1
        else:
            keep = chr(random.randint(0,5)+107)
            if (keep == "k"):
                c = c + tempscore + roll
                player = player * -1
            else:
                tempscore = tempscore + roll
                ccount = ccount + 1
    print("@ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ ")
    print(t+"GAME OVER")
    print(t+"HUMAN TOTAL = "+str(h)+" COMPUTER TOTAL = "+str(c))
    print(t+"TOTAL ROLLS : HUMAN = "+str(hcount)+" COMPUTER = "+str(ccount))
    print("@ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ ")

if __name__=="__main__":
    main()

'''
NOTES:
h (human total)  c(computer total)
player (this variable will be -1 or 1 -1 is human 1 is computer)
hcount counts the human rolls and ccount counts the comouter rolls
'''
