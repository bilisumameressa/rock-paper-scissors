import random

players = [
    {
        "type": "user",
        "choice": user_choice
    },
    {
        "type": "computer",
        "choice": computer_choice
    }
]

def winner(player1, player2):
    if player1 == player2:
        return False
    elif player1 == "R":
        if player2 == "P":
            return player2
        elif player2 == "S"
            return player1
    elif player1 == "P":
        
    elif player1 == "S":
    
        

def play():
    choices = ["R", "P", "S"]
    computer_choice = random.choice(choices)
    user_choice = input("R, P, S: ")
    
    print("You chose: " + user_choice)
    print("Computer chose: " + computer_choice)
    
    

