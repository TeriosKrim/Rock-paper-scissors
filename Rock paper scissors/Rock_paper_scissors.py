from random import randint

#Create a list of play to the computer
t = ["rock", "paper", "scissors"]

#Assign a random play to the computer

computer = t[randint(0,2)]

#Set player to false
player = False

#This asks the player if that want to play again


while player == False:
    #Set player to true
    player = input("rock, paper, or scissor ")
    if player == computer:
        print("TIE! Go again")
    elif player == "rock":
        if computer == "Paper":
            print("YOU LOSE....", computer, "Covers", player)
            
        elif computer == "Rock":
            print("TIE! Go again")
        else:
            print("YOU WIN!!!", player, "Smashes", computer)
            


    elif player == "paper":
        if computer == "scissor":
            print("YOU LOSE..", computer, "Cuts", player)
            
        elif computer == "paper":
            print("TIE! Go again")

        else:
            print("YOU WIN!!", player, "Covers", computer)
            


    elif player == "scissor":
        if computer == "rock":
            print("YOU LOSE.", computer, "Smashes", player)
           

        elif computer == "scissor":
            print("TIE! Go again")
        else:
            print("YOU WIN!!", player, "Cuts", computer)
            


    else:
        print("NOT A VALID PLAY PLEASE CHECK SPELLING")
        #player was set to true make it false so the loop can continue
    player = False
    computer = t[randint(0,2)]

  

    if input == 'n':
        break

