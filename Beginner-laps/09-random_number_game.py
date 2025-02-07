# logic: computer will generate a random choice & compare it against your choice

import random

user_choice = int(input("What do you choose? \nType 0, 1 or 2.\n"))
computer_choice = random.randint(0 , 2)
print(f"Computer chose: {computer_choice}")

if computer_choice == user_choice:
    print("It's a drow!")
elif user_choice > 2:
    print("You entered invalid number, You lose!")
else:
    print("You Lose!")