import random

choices = ["R", "P", "S"]
        
while True:
    CPU = random.choice(choices)
    Player = input("R for Rock, P for Paper or S for Scissors? ").upper()
    
    if Player == CPU:
        print("Player ({}) : CPU ({})" .format(Player, CPU))
        print("Draw !!")
    
    elif Player == "P":
        if CPU == "R":
            print("Player ({}) : CPU ({})" .format(Player, CPU))
            print("Player Wins !")
            break
        if CPU == "S":
            print("Player ({}) : CPU ({})" .format(Player, CPU))
            print("Computer Wins !")
            break
                
    elif Player == "R":
        if CPU == "S":
            print("Player ({}) : CPU ({})" .format(Player, CPU))
            print("Player Wins !")
            break
        if CPU == "P":
            print("Player ({}) : CPU ({})" .format(Player, CPU))
            print("Computer Wins !")
            break
                
    elif Player == "S":
        if CPU == "P":
            print("Player ({}) : CPU ({})" .format(Player, CPU))
            print("Player Wins !")
            break
        if CPU == "R":
            print("Player ({}) : CPU ({})" .format(Player, CPU))
            print("Computer Wins !")
            break
    else:
        print("Check your input")