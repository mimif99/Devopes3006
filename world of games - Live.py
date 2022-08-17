def welcome(name):
    return f"Hello {name} and welcome to the World of Games (WoG).\nHere you can find many cool games to play.\n"

def load_game():
    a = '0'
    print("you have three options:  \n 1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back.  \n 2. Guess Game - guess a number and see if you chose like the computer  \n 3. Currency Roulette - try and guess the value of a random amount of USD in ILS")
    level = input("Please choose a game to play: ")
    if level == "1":
        print("You chose the Memory Game ")
        # fun1()
    elif level == "2":
        print("You chose the Guess Game")
        # fun2()
    elif level == "3":
        print("You chose the Currency Roulette Game")
        # fun3()
    else:
        print("You must choose between 1 or 2 or 3")
        return load_game()

    print("\nPlease choose game difficulty from 1 to 5")
    while a < '1' or a > '5':
        a = input("Enter your choice: ")