#cwc
import random
def display(roll,tempscore,player,count,h,c):
    trow = "* * * * * * * * * * * * * * * * * * * * * * * * *"
    if(player == -1):
        t="*\t"
        playerName = "HUMAN"
    else:
        t= "*\t\t\t"
        playerName = "COMPUTER"
    #print(t+"roll  count  h  c")
    print(trow)
    print(t+"PLAYER "+playerName)
    print(t+"ROLL VALUE "+str(roll)+" CURRENT ROLL SCORE "+str(tempscore))
    print(trow)
    if (player == -1):
        print(t+"HUMAN")
    else:
        print("\t\t\tCOMPUTER")
def main():
    h = 0;c = 0; tempscore = 0; player = -1
    print("LET'S GET STARTED")
    print("TYPE K OR k to KEEP YOUR SCORE")
    print("TYPE ANY OTHER CHARACTER TO ROLL")
    print("THEN PRESS THE \'Enter\' KEY\n\n")
    while (h < 100 or c < 100):
        count = 1
        keep = "*"
        roll = random.randint(1,6)
        display(roll,tempscore,player,count,h,c)
        if (roll == 1):
            tempscore = 0
            player = player * -1
        elif(player == -1):
            keepTheScore = input ("Keep the score ?")
            keep =  keepTheScore[0].lower()
            if (keep == 'k'):
                h= h + tempscore + roll
                player = player * -1
            else:
                tempscore = tempscore + roll
        else:
            keep = chr(random.randint(0,5)+107)
            if (keep == "k"):
                c = c + tempscore + roll
                player = player * -1
            else:
                tempscore = tempscore + roll

if __name__=="__main__":
    main()
