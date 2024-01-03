import random

def play():
    choices = ["R", "P", "S"]
    computer = random.choice(choices)
    user = input("R, P, S: ")

    draw_message = "Its a draw!"
    user_wins_message = "You won!"
    computer_wins_message = "Computer wins!"
    
    print("You chose: " + user)
    print("Computer chose: " + computer)
    
    if  user == computer:
        return draw_message
    elif  user == "R":
        if computer == "P":
            return computer_wins_message
        elif computer == "S":
            return user_wins_message
    elif user == "P":
        if computer == "R":
            return user_wins_message
        elif computer == "S":
            return computer_wins_message
    elif user == "S":
        if computer == "P":
            return user_wins_message
        elif computer == "R":
            return computer_wins_message

print(play())

while True:
    want_to_play = input("Press any key to play, Q to exit: ")
    if want_to_play == "Q":
        break
    else:
        print(play())

    
    
    
    
    

