print("Welcome to Pizza pricing calculator")
# price is based on size and extra pepperoni or extra cheese
size = input("what pizza size do you want? S, M OR L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you eant extra cheese? Y or N: ")
price = 0  # intial price holder

if size == "S":
    price = 15
    if pepperoni == "Y":
        price +=2
elif size == "M":
    price = 20
    if pepperoni == "Y":
        price +=3
elif size == "L":
    price = 25
    if pepperoni == "Y":
        price +=3
else:
    print("Invalid input")

if extra_cheese == "Y":
    price +=1

print(f"Price = {price}")