#Exercise 8:
# Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)
a = ["Rock","Paper","Scissors"]
while(True):
    p1 = input("Player1 enter your Rock-Paper-Scissors:")
    while(True):
        if(p1 in a):
            break
        else:
            p1 = input("Enter valid response:")
    p2 = input("Player2 enter your Rock-Paper-Scissors:")
    while(True):
        if(p2 in a):
            break
        else:
            p2 = input("Enter valid response:")
    print("Congrats Players")
    cmd = input("wanna play again enter y")
    if(cmd == "y"):
        continue
    else:
        break
