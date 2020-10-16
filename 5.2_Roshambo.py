'''
ROSHAMBO PROGRAM
----------------

Create a program that randomly prints 1, 2, or 3.
Expand the program so it randomly prints rock, paper, or scissors using if statements. Don't select from a list.
Add to the program so it first asks the user their choice as well as if they want to quit.
(It will be easier if you have them enter 1 for rock, 2 for paper, and 3 for scissors.)
Add conditional statements to figure out who wins and keep the records
When the user quits print a win/loss record

'''
import random
x = 0
game = 1
win = 0
loss = 0
draw = 0
print("Welcome to rock, paper, scissors. Enter a 1 for rock, 2 for scissors, and a 3 for paper. The game will keep a record of your wins/losses.")
while x < 1:
    print()
    print("Game",game,"")
    print()
    choice = int(input("Your Choice: "))
    compchoice = random.randrange(1,4,1)
    if choice == 1:
        print("Your Move: Rock")
    elif choice == 2:
        print("Your Move: Paper")
    elif choice == 3:
        print("Your Move: Scissors")
    if compchoice == 1:
        print("Computer Move: Rock")
    elif compchoice == 2:
        print("Computer Move: Paper")
    elif compchoice == 3:
        print("Computer Move: Scissors")
    if choice == 1 and compchoice == 1:
        print("DRAW")
    elif choice == 2 and compchoice == 2:
        print("DRAW")
    elif choice == 3 and compchoice == 3:
        print("DRAW")
    elif choice == 1 and compchoice == 3:
        win += 1
        print("WIN")
        again = input("PLAY AGAIN? (Y OR N): ")
        if again.upper() == "N":
            x += 1
        elif again.upper() == "Y":
            x == 0
            game += 1
    elif choice == 2 and compchoice == 1:
        win += 1
        print("WIN")
        again = input("PLAY AGAIN? (Y OR N): ")
        if again.upper() == "N":
            x += 1
        elif again.upper() == "Y":
            x == 0
            game += 1
    elif choice == 3 and compchoice == 2:
        win += 1
        print("WIN")
        again = input("PLAY AGAIN? (Y OR N): ")
        if again.upper() == "N":
            x += 1
        elif again.upper() == "Y":
            x == 0
            game += 1
    elif choice == 1 and compchoice == 2:
        loss += 1
        print("LOSS")
        again = input("PLAY AGAIN? (Y OR N): ")
        if again.upper() == "N":
            x += 1
        elif again.upper() == "Y":
            x == 0
            game += 1
    elif choice == 2 and compchoice == 3:
        loss += 1
        print("LOSS")
        again = input("PLAY AGAIN? (Y OR N): ")
        if again.upper() == "N":
            x += 1
        elif again.upper() == "Y":
            x == 0
            game += 1
    elif choice == 3 and compchoice == 1:
        loss += 1
        print("LOSS")
        again = input("PLAY AGAIN? (Y OR N): ")
        if again.upper() == "N":
            x += 1
        elif again.upper() == "Y":
            x == 0
            game += 1
games = win+loss
winratio = win/games
winratio *= 100
print("Wins: ",win)
print("Losses: ",loss)
print()
print("Win Percentage: ",winratio,"%")


