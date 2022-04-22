from tkinter.messagebox import YES
from time import sleep


print("Welcome to the Cabin in the Woods!")

# First, we welcome the player.
player_name = str(input("How would you like to be called: ")).strip()
player_age = int(input("Please, enter your age: "))
print(f"\nHello {player_name}!\nYou're {player_age} years old.")

health = 100

# Let's confirm if they wwant to start.
game_start = str(input("\nDo you wish to start? ")).upper().strip()
if game_start == "YES":
    sleep(1)
    print("\nSo be it, then...")
    sleep(1)
    print("Level One")
    sleep(1)
    print("The Forest!")
    sleep(1)
    print(
        f"You are {player_name}, an {player_age} years old adventurer.\n"
        "\nIn search of the truth. you threw yourself into the unknown... but was it a good idea?.\n"
        f"\nYou have {health} life points.\n"
    )

    # This is the body of our game, where it starts!
    while health > 0:
        print("-=-" * 35)
        sleep(8)
        print(
            "It's cold and raining, the sound of the water falling on "
            "the trees mixes with the sound of the animals."
        )
        sleep(8)
        print(
            "\nYou don't know where you are or how you got here, "
            "but you know one thing, you're not safe!"
        )
        sleep(8)
        print(
            "\nYou decide to seek shelter from the rain, "
            "there's no time to look for an answer, not now."
        )
        sleep(8)
        print(
            "\nWhen nwalking through the dark forest, "
            "you hear frightening noises, you better hurry."
        )
        sleep(10)
        print(
            "\nAfter walking for a bit, you find a cave, maybe you can spend the night here, "
            "\nmake a fire and wait for the rain to stop. Get help in the morning..."
        )
        sleep(5)
        print("But is it safe?")
        print("\nWould it be better to go on and try to find a better place?\n")
        sleep(8)
        choice_01 = int(
            input(
                "Explore the cave or continue through the forest?"
                "\nPlease enter [0] for Forest or [1] for Cave\n"
            )
        )

        # This is our first choice, now our game will split!
        # If the player chose to continue:
        if choice_01 == 0:
            sleep(10)
            print(
                "As you approach the cave you hear a kind of grunt,  it could be a bear.\n"
                "Or some other dangerous animal, maybe something even worse...\n"
            )
            sleep(8)
            print("\nIt's better to keep walking!\n")
            print(
                "You keep exploring the forest. When you see a light between the trees."
            )
            sleep(1)
            print("Is it...! ")
            sleep(2)
            print("is a...")
            sleep(3)
            print("A cabin!")
            print(
                "And if there's light, there are people, and maybe they'll offer me food and shelter."
            )
            print("Well, you don't have much choice here in the woods, so...")
            print("You head towards the cabin!")
            print("As you approached the cabin, the clouds got darker...")
            sleep(7)
            print(
                "The rain seemed to be getting worse, but there was something else..."
            )
            print("Something you couldn't explain...")
            sleep(10)
            print("As you approached the cabin you noticed something strange...")
            print("Something that shouldn't be there.")
            sleep(5)
            print("...")
            sleep(10)
            print(
                "Your stomach started to churn, a feeling of nausea...\n"
                "You wanted to get out of there... maybe you should have..."
            )
            sleep(10)
            print("But when you get a few meters from the door...")
            sleep(10)
            print("It opens...")
            sleep(5)
            print("And there's someone at the door waiting for you...")
            sleep(5)
            print(f"The person says: Come {player_name}... we were waiting for you!")
            print("So you understand... you saw...")
            sleep(10)
            print("But you wish you never had!")
            sleep(5)
            print("To be continued...")
            break

        # If he chose the cave:
        elif choice_01 == 1:
            sleep(1)
            print(
                "It's very cold, and if you continue to wander aimlessly through the rain,\n"
                "you could end up dying of hypothermia!"
            )
            sleep(1)
            print("\nBetter take shelter in that cave!\n")
            sleep(1)
            print("You enter the cave and notice that it has some tracks on the floor.")
            sleep(1)
            print("Apparently it must be an old abandoned mine!")
            sleep(1)
            print("You are hungry and wet.")
            sleep(1)
            print(
                "The cave is colder than the devil's heart and the wind, "
                "which enters whistling like the sound of nymphs, "
                "cuts his body like the knife that pierced Cesar."
            )
            print(5)
            print(
                "Maybe you can find something, inside the mines, something to make a fire!"
            )
            sleep(5)
            print("You enter the darkness, when you notice something peculiar...")
            sleep(5)
            print("A faint little glow, coming from the darkness, maybe it's...")
            sleep(5)
            print("Will it be?")
            sleep(5)
            print("To be continued...")
            break

        #
        else:
            error01 = input("Please enter a valid choice")
            continue


# If no, the game end u.u
else:
    print("\nOk. See you, Space Cowboy")
