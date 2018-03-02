import random
play=str(input("Do you want to play Game (Y/N)?:"))
while play=="Y" or play=="y":
#    game()
#def game():
    print("\nEnter 1 for Rock \nEnter 2 for Paper \nEnter 3 for Scissors \n")
#1=Rock
#2=Paper
#3=Scissors
    userInput=int(input("Enter your play: "))
              
    computer_Input = random.randint(1,3)
#    print(computer_Input)

    if userInput==1:
        if userInput==computer_Input:
            print("The Game is Draw, Play again\n")
        elif computer_Input>2:
            print("You Won, Rock beats scissors\n")
        else:
            print("You Lose, Paper beats rock\n")

    if userInput==2:
        if userInput==computer_Input:
            print("The Game is Draw, Play again\n")
        elif computer_Input<2:
            print("You Won, Paper beats rock\n")
        else:
            print("You Lose, Scissors beats paper\n")
    if userInput==3:
        if userInput==computer_Input:
            print("The Game is Draw, Play again\n")
        elif computer_Input<2:
            print("You Lose, Rock beats scissors\n")
        else:
            print("You Won, Scissors beats paper\n")
    if userInput>3:
        print("Enter a Valid Value\n")
    play=str(input("Do you want to play another Game (Y/N)?:"))

