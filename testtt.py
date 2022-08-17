name = input('Please enter your name: ')
for i in name:
    if name.isalpha() == False:
        print('Please enter a alphabetical name')
        return
    else:
    print(f"Hello {name} and welcome to the World of Games (WoG). \n Here you can find many cool games to play.")
        pass


def welcome():
    while True:
        name = input("Please enter your name: ")
        if name.isalpha() == False:
            print('Please enter a alphabetical name')
            break
        else:
            print("Please enter a alphabetical name")


print(welcome("Guy"))



