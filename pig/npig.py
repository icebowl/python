#cwc
import random
def display(roll,tempscore,player,count,h,c):
    if(player == -1):
        t=""
    else:
        t= "\t\t\t"
    print(t+"roll  count  h  c")
    print(t,roll,tempscore,player,count,h,c)
    if (player == -1):
        print("HUMAN")
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
            keepTheScore = input ("Keep?")
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
