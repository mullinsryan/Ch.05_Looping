'''
CAMEL GAME
----------
The pseudo-code for how to code this game is in Chapter 5 of the Python Jedi book

'''
import random
distance = 200
shark_distance = 50
x = 0
y = 0
health = 10
hunger = 0
turn = 1
while x < 1:
    #Instructions
    print("Welcome to the fish game.")
    print()
    print("You are a small fish trying to travel across the ocean during migration season.")
    print("A nearby group of sharks knows you are doing this, and they are hungry.")
    print("Your goal is to travel 200 m to your pod of fish without getting caught by the sharks.")
    print("Every interval, you will be asked commands.")
    print("\n\nCommands:")
    print("     1. Swim quickly")
    print("     2. Swim moderately")
    print("     3. Swim slowly")
    print("     4. Rest")
    print("     5. Check status")
    print("     6. Eat")
    print("\nEnter a number to execute a command (That means you Jake).")
    print("\nChecking status is free and will not effect the game.")
    print("\nYou can only eat when you have food.")
    begin = input("\nTo begin, press enter...")

    while distance > 0:

        print("Turn",turn)
        event_numb = random.randrange(1,6,1)
        command = int(input("What is your command: "))
        if command == 1:
            distance -= 20
            hunger += 2
            print("You swam quickly and traveled 20 m")
            if event_numb == 3:
                print("You weren't paying attention and swam into an unhelpful current.")
                distance += 10
            elif event_numb == 4:
                print("You took advantage of helpful currents.")
                distance -=10
            elif event_numb == 5:
                print("You collided with another fish and damaged your fins.")
                health -= 2
                print("Health:",health,"/10")
            print("You have",distance,"m left.")
            turn += 1
        elif command == 2:
            distance -= 15
            hunger += 1
            print("You swam moderately and traveled 15 m.")
            
            print("You have",distance,"m left.")
            turn += 1
        elif command == 3:
            distance -= 10
            hunger += 0.5
            print("You swam slowly and traveled 10 m.")
            print("You have", distance, "m left.")
            turn += 1
        elif command == 4:
            print("You stopped to rest.")
            hunger += 1
            if health < 10:
                health +=1
                turn += 1
            else:
                print("Your health is full.")
                turn += 1
        elif command == 5:
            print("Distance Left:",distance,"m")
            print("Health:",health,"/10")
            print("Hunger:",hunger,"/10")
        elif command == 6:
            print("You ate your food.")
            hunger -= 1
            print("Hunger: ", hunger, "/10")
            turn += 1
            if hunger == 0:
                print("You are not hungry.")

    print("Congratulations. You made it to the destination and finished the game.")
    x += 1
















