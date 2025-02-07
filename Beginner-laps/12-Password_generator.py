#Password Generator Project
import random
print("Welcome to the PyPassword Generator!")

# deine the values that can be used in the password
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# ask for the needed password
numbers_of_letters = int(input("How many letters would you like in your password? ")) 
numbers_of_symbols = int(input(f"How many symbols would you like? "))
numbers_of_numbers = int(input(f"How many numbers would you like? "))

password_holder = []
for letter in range(1, numbers_of_letters + 1):
    password_holder.append(random.choice(letters))

for symbol in range(1, numbers_of_symbols + 1):
    password_holder.append(random.choice(symbols))

for number in range(1, numbers_of_numbers + 1):
    password_holder.append(random.choice(numbers))

# password_holder now has the values in order chars, symbols, numbers
# to change that order randomly
random.shuffle(password_holder)
# Convert a list into string
password = ""
for element in password_holder:
    password += element

print(f"Your password is: {password}")
