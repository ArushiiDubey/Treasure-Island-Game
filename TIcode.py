print('''
*******************************************************************************
 _                                     _     _                 _ 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|
                                                                 
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
character= input("choose a character: knight , huntsman, prince")
print(f"There once lived a prosperous king, on his deathbed he told you {character} the path to his hidden treasure.")
print(f"On your way to the treasure you come across a bear : the guardian of the treasure \n Let\'s see oh {character} whether you can reach the treasure or not " )
choice1 = input('You\'re at a crossroad, where do you want to go? '
                'Type "left" or "right".\n').lower()

if choice1 == "left":
    choice2 = input('You\'ve come to a lake. '
                    'There is an island in the middle of the lake. '
                    'Type "wait" to wait for a boat. '
                    'Type "swim" to swim across.\n').lower()
    if choice2 == "wait":
        choice3 = input("You arrive at the island unharmed. "
                        "There is house with 3 doors. One red, "
                        "one yellow and one blue. "
                        "Which colour do you choose?\n").lower()
        if choice3 == "red":
            print(f"It's a room full of fire. Game Over {character}")
        elif choice3 == "yellow":
            print(f"You found the treasure. You Win {character}!")
        elif choice3 == "blue":
            print(f"You enter a room of beasts. Game Over {character}.")
        else:
            print(f"You chose a door that doesn't exist. Game Over {character}.")
    else:
        print(f"You got attacked by a shark. Game Over {character}.")

else:
    print(f"You got eaten by a bear. Game Over {character}.")