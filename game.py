import random
rock = 1
paper = 2
scissors = 3

while True:
    npc = random.randint(1, 3)  
    player = input("Enter rock, paper, or scissors: ").lower()

    if rock == npc and player == "rock":
        print("The Computer picked rock. draw")
    elif rock == npc and player == "paper":
        print("The Computer picked rock. you win")
    elif rock == npc and player == "scissors":
        print("The Computer picked rock. you lose")
    if paper == npc and player == "rock":
        print("The Computer picked paper. you lose")
    elif paper == npc and player == "paper":
        print("The Computer picked paper. draw")
    elif paper == npc and player == "scissors":
        print("The Computer picked paper. you win")
    if scissors == npc and player == "rock":
        print("The Computer picked scissors. you win")
    elif scissors == npc and player == "paper":
        print("The Computer picked scissors. you lose")
    elif scissors == npc and player == "scissors":
        print("The Computer picked scissors. draw")

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        break