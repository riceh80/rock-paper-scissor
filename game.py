import random

npc = random.randint(1, 3)
player = input("rock, paper, or scissors? ")
rock = 1
paper = 2
scissors = 3
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
