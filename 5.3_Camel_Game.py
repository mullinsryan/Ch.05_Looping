'''
CAMEL GAME
----------
The pseudo-code for how to code this game is in Chapter 5 of the Python Jedi book

'''
import random
distance = 200
shark_distance = 30
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

    while distance > 0 and hunger < 10 and health > 0 and shark_distance > 0:

        print("     Turn",turn)
        event_numb = random.randrange(1,6,1)
        shark_numb = random.randrange(1,4,1)
        command = int(input("What is your command: "))
        if command == 1: #Command 1
            distance -= 20
            hunger += 2
            print("You swam quickly and traveled 20 m")
            if event_numb == 2 or event_numb == 1:
                print("You found some food.")
            if event_numb == 3:
                print("You swam into an unhelpful current.")
                distance += 10
            elif event_numb == 4:
                print("You took advantage of helpful currents.")
                distance -=10
            elif event_numb == 5:
                print("You collided with another fish and damaged your fins.")
                health -= 2
                print("Health:",health,"/10")
            if shark_numb == 1:
                shark_distance -= 2
                print("Shark Distance:", shark_distance, "m")
            elif shark_numb == 2:
                print("Shark Distance:",shark_distance,"m")
            else:
                shark_distance += 5
                print("Shark Distance:", shark_distance, "m")
            print("You have",distance,"m left.")
            turn += 1
        elif command == 2: #Command 2
            distance -= 15
            hunger += 1
            print("You swam moderately and traveled 15 m.")
            if event_numb == 2 or event_numb == 1:
                print("You found some food.")
            if event_numb == 3:
                print("You swam into an unhelpful current.")
                distance += 10
            elif event_numb == 4:
                print("You took advantage of helpful currents.")
                distance -=10
            elif event_numb == 5:
                print("You collided with another fish and damaged your fins.")
                health -= 2
                print("Health:", health, "/10")
            if shark_numb == 1:
                shark_distance -= 4
                print("Shark Distance:", shark_distance, "m")
            elif shark_numb == 2:
                shark_distance -= 2
                print("Shark Distance:", shark_distance, "m")
            else:
                print("Shark Distance:",shark_distance,"m")
            print("You have",distance,"m left.")
            turn += 1
        elif command == 3:
            distance -= 10
            hunger += 0.5
            print("You swam slowly and traveled 10 m.")
            if event_numb == 2 or event_numb == 1:
                print("You found some food.")
            if event_numb == 3:
                print("You swam into an unhelpful current.")
                distance += 10
            elif event_numb == 4:
                print("You took advantage of helpful currents.")
                distance -=10
            elif event_numb == 5:
                print("You collided with another fish and damaged your fins.")
                health -= 2
                print("Health:", health, "/10")
            if shark_numb == 1:
                shark_distance -= 8
                print("Shark Distance:", shark_distance, "m")
            elif shark_numb == 2:
                shark_distance -= 4
                print("Shark Distance:", shark_distance, "m")
            else:
                shark_distance -= 3
                print("Shark Distance:",shark_distance,"m")
            print("You have", distance, "m left.")
            turn += 1
        elif command == 4:
            print("You stopped to rest.")
            hunger += 1
            if health < 10:
                health = 10
                turn += 1
            else:
                print("Your health is full.")
            if event_numb == 3:
                print("You swam into an unhelpful current.")
                distance += 10
            elif event_numb == 4:
                print("You took advantage of helpful currents.")
                distance -=10
            elif event_numb == 5:
                print("You collided with another fish and damaged your fins.")
                health -= 2
                print("Health:", health, "/10")
            if shark_numb == 1:
                shark_distance -= 15
                print("Shark Distance:", shark_distance, "m")
            elif shark_numb == 2:
                shark_distance -= 10
                print("Shark Distance:", shark_distance, "m")
            else:
                shark_distance -= 8
                print("Shark Distance:",shark_distance,"m")
        elif command == 5:
            print("Distance Left:",distance,"m")
            print("Health:",health,"/10")
            print("Hunger:",hunger,"/10")
        elif command == 6:
            if hunger == 0:
                print("You are not hungry.")
            else:
                print("You ate your food.")
                hunger = 0
                print("Hunger: ", hunger, "/10")
                turn += 1
            if shark_numb == 1:
                shark_distance -= 15
                print("Shark Distance:", shark_distance, "m")
            elif shark_numb == 2:
                shark_distance -= 10
                print("Shark Distance:", shark_distance, "m")
            else:
                shark_distance -= 8
                print("Shark Distance:",shark_distance,"m")


    if distance <= 0 and hunger < 10 and health > 0 and shark_distance > 0:
        print("Congratulations. You made it to the destination and finished the game.\nWIN")
        x += 1
    elif hunger >= 10:
        print("You got too hungry to continue.\nLOSS")
        x += 1
    elif health <= 0:
        print("Your health got too low to keep swimming.\nLOSS")
        x += 1
    elif shark_distance <= 0:
        print("The sharks got you.\nLOSS")
        x += 1

















