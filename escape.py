# mini text based escape game

def print_help(self):
    print("The help menu")
    print("-------------")
    print("R = Reset")
    print("E = Exit")
    print("H = Help")

# define level count
current_level = 1

while current_level <= 5:
    print("-------------")
    # ask for input
    print(f"Your current level: {current_level}")
    user_input = input("Your answer: ")

    if user_input == "Yes":
        current_level += 1
        print("Right answer, next level!")
    elif user_input == "H":
        print_help("")
    elif user_input == "R":
        current_level = 0
    else:
        print("Wrong answer, try again.")

else:
    print("Congratulations, you're done!")
