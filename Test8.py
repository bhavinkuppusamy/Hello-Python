import random
totalGames=0
won=0
lose=0
tie=0
play=str(input("Do you want to play Game (Y/N)?:"))
while play=="Y" or play=="y":
#    game()
#def game():
#1=Rock
#2=Paper
#3=Scissors

    print("\nEnter 1 for Rock \nEnter 2 for Paper \nEnter 3 for Scissors \n")

    userInput=int(input("Enter your play: "))
    if userInput<4:
        totalGames+=1              
    computer_Input = random.randint(1,3)
#    print(computer_Input)

    if userInput==1:
        if userInput==computer_Input:
            print("The Game is Draw, Play again\n")
            tie+=1
        elif computer_Input>2:
            print("You Won, Rock beats scissors\n")
            won+=1
        else:
            print("You Lose, Paper beats rock\n")
            lose+=1

    if userInput==2:
        if userInput==computer_Input:
            print("The Game is Draw, Play again\n")
            tie+=1
        elif computer_Input<2:
            print("You Won, Paper beats rock\n")
            won+=1
        else:
            print("You Lose, Scissors beats paper\n")
            lose+=1
            
    if userInput==3:
        if userInput==computer_Input:
            print("The Game is Draw, Play again\n")
            tie+=1
        elif computer_Input<2:
            print("You Lose, Rock beats scissors\n")
            lose+=1
        else:
            print("You Won, Scissors beats paper\n")
            won+=1
            
    if userInput>3:
        print("Enter a Valid Value\n")
    play=str(input("Do you want to play another Game (Y/N)?:"))
    
print("Total number of Games played :",totalGames)
print(won,"won",lose,"Lost",tie,"Tie")
