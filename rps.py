#!/usr/bin/env python3
import random
import time

#output
print("\n")
print("Welcome to Rock, Paper, Scissors!")
print("=================================")

#for winner text
bold = '\033[1m'
end = '\033[0m'

#variable to determine whether the user wishes to play again or not
play = "y"

#scoreboard variables
wins=0
losses=0
ties=0

urockCounter=0
upaperCounter=0
uscissorsCounter=0

uWinWithRock=0
uWinWithPaper=0
uWinWithScissors=0
cWinWithRock=0
cWinWithPaper=0
cWinWithScissors=0

cpuRCount=0
cpuPCount=0
cpuSCount=0

rBestPick=0
pBestPick=0
sBestPick=0

while (play == "y") : 
    #player move
    playerChoice = input("\nEnter 1 (Rock), 2 (Paper), or 3 (Scissors): ")

    #computer move
    cpuChoice = random.randint(1, 3)
   
    #player chooses rock
    if playerChoice == "1":
        urockCounter+=1
        if cpuChoice == 1:
            cpuRCount+=1
            print("Rock vs Rock...")
            pBestPick+=1
            print(bold + "Its a tie!" + end,"\n")
            ties+=1
        elif cpuChoice == 2:
            cpuPCount+=1
            print("Rock vs Paper...")
            sBestPick+=1
            print(bold + "You lost!" + end,"Paper covers rock.\n")
            cWinWithPaper+=1
            losses+=1
        elif cpuChoice == 3:
            cpuSCount+=3
            print("Rock vs Scissors...")
            rBestPick+=1
            print(bold + "You won!" + end,"Rock smashes scissors.\n")
            uWinWithRock+=1
            wins+=1
    elif playerChoice == "2":
        upaperCounter+=1
        if cpuChoice == 1:
            cpuRCount+=1
            print("Paper vs Rock...")
            pBestPick+=1
            print(bold + "You won!" + end,"Paper covers rock.\n")
            uWinWithPaper+=1
            wins+=1
        elif cpuChoice == 2:
            cpuPCount+=1
            print("Paper vs Paper...")
            sBestPick+=1
            print(bold + "Its a tie!" + end,"\n")
            ties+=1
        elif cpuChoice == 3:
            cpuSCount+=1
            print("Paper vs Scissors...")
            rBestPick+=1
            print(bold + "You lost!" + end,"Scissors cuts paper.\n")
            cWinWithScissors+=1
            losses+=1
    elif playerChoice == "3":
        uscissorsCounter+=1
        if cpuChoice == 1:
            cpuRCount+=1
            print("Scissors vs Rock...")
            pBestPick+=1
            print(bold + "You lost!" + end,"Rock smashes scissors.\n")
            cWinWithRock+=1
            losses+=1
        elif cpuChoice == 2:
            cpuPCount+=1
            print("Scissors vs Paper...")
            sBestPick+=1
            print(bold + "You won!" + end,"scissors cuts paper.\n")
            uWinWithScissors+=1
            wins+=1
        elif cpuChoice == 3:
            cpuSCount+=1
            print("Scissors vs Scissors...")
            rBestPick+=1
            print(bold + "Its a tie!" + end,"\n")
            ties+=1

    #invalid input check
    else:
        print("Invalid Input. Please try again and enter 1, 2, or 3\n")

    #play again check
    play = input("Do you wish to play again? (y = yes, n = no): ")

###############################################################
#statistics output
print("\n")
print("Statistics:")
print("===========")

###############################################################
print("\nWins & Losses:")
print("Wins:   ",wins)
print("Losses: ",losses)
print("Ties:   ",ties)

###############################################################
print("\nUser Choices:")
print("Rock:     ",urockCounter)
print("Paper:    ",upaperCounter)
print("Scissors: ",uscissorsCounter)

###############################################################
print("\nGame Data Log:")
userMostWon = "temp"
cpuMostWon = "temp"

###User most won calculation###
if (uWinWithRock > uWinWithPaper) and (uWinWithRock > uWinWithScissors):
    userMostWon = "Rock"
elif (uWinWithPaper > uWinWithRock) and (uWinWithPaper > uWinWithScissors):
    userMostWon = "Paper"
elif (uWinWithScissors > uWinWithRock) and (uWinWithScissors > uWinWithPaper):
    userMostWon = "Scissors"

#2 = most won
if (uWinWithRock == uWinWithPaper) and (uWinWithRock > uWinWithScissors):
    userMostWon = "Rock and Paper"
elif (uWinWithRock == uWinWithScissors) and (uWinWithRock > uWinWithPaper):
    userMostWon = "Rock and Scissors"
elif (uWinWithPaper == uWinWithScissors) and (uWinWithPaper > uWinWithRock):
    userMostWon = "Paper and Scissors"

#all 3 = most won
if (uWinWithRock == uWinWithPaper) and (uWinWithRock == uWinWithScissors):
    userMostWon = "Rock, Paper, and Scissors"


###Cpu most won calculation###
if (cWinWithRock > cWinWithPaper) and (cWinWithRock > cWinWithScissors):
    cpuMostWon = "Rock"
elif (cWinWithPaper > cWinWithRock) and (cWinWithPaper > cWinWithScissors):
    cpuMostWon = "Paper"
elif (cWinWithScissors > cWinWithRock) and (cWinWithScissors > cWinWithPaper):
    cpuMostWon = "Scissors"

#2 = most won
if (cWinWithRock == cWinWithPaper) and (cWinWithRock > cWinWithScissors):
    cpuMostWon = "Rock and Paper"
elif (cWinWithRock == cWinWithScissors) and (cWinWithRock > cWinWithPaper):
    cpuMostWon = "Rock and Scissors"
elif (cWinWithPaper == cWinWithScissors) and (cWinWithPaper > cWinWithRock):
    cpuMostWon = "Paper and Scissors"

#all 3 = most won
if (cWinWithRock == cWinWithPaper) and (cWinWithRock == cWinWithScissors):
    cpuMostWon = "Rock, Paper, and Scissors"

if wins > losses:
    print("The player won more rounds (",wins,")")
    print("They won with",userMostWon,"the most")
elif wins < losses:
    print("The CPU won more rounds (",losses,")")
    print("They won with",cpuMostWon,"the most")
elif wins == losses:
    print("The Player and CPU had the same number of wins (",wins,")")
    print("The Player won with",userMostWon,"the most")
    print("The CPU won with",cpuMostWon,"the most")

###############################################################
#Checking for 1 best pick
bestPossiblePick = "temp"
if (rBestPick > pBestPick) and (rBestPick > sBestPick):
    bestPossiblePick = "Rock"
elif (pBestPick > rBestPick) and (pBestPick > sBestPick):
    bestPossiblePick = "Paper"
elif (sBestPick > rBestPick) and (sBestPick > pBestPick):
    bestPossiblePick = "Scissors"

#Checking for 2 best picks
if (rBestPick == pBestPick) and (rBestPick > sBestPick):
    bestPossiblePick = "Rock and Paper"
elif (rBestPick == sBestPick) and (rBestPick > pBestPick):
    bestPossiblePick = "Rock and Scissors"
elif (pBestPick == sBestPick) and (pBestPick > rBestPick):
    bestPossiblePick = "Paper and Scissors"

#Checking for 3 best picks
if (rBestPick == pBestPick) and (rBestPick == sBestPick):
    bestPossiblePick = "Rock, Paper, and Scissors all"
print(bestPossiblePick,"would have had the most success against the CPU.\n")

#end statistics output
print("==============================================================================\n")
###END PROGRAM###
