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


