"""
check if a user can play rollercoster or not
user is allowed if his height greater then 120 cm

the pricing list is
5$ if age less than 12
7$ if age between 12 and 18
12$ if above 18
"""
print("Welcome to the rollercoster")

height = int(input("What's your height in cm? "))

if height >= 120:
    age = int(input("What's your age? "))
    if age <= 12:
        print("Please pay $5")
    elif age <=18:
        print("Please pay $7")
    else:
        print("Please pay $12")
else:
    print("You are not allowed to ride the rollercoaster")


