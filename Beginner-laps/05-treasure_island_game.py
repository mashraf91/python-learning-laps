# Treasure island game - flow chart https://viewer.diagrams.net/index.html?highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload#%7B%22pageId%22%3A%22C5RBs43oDa-KdzZeNtuy%22%7D
# You can get animation art from https://ascii.co.uk/art

print("""
                                                    ____
                                         v        _(    )
        _ ^ _                          v         (___(__)
       '_\\V/ `
       ' oX`
          X                            v
          X                                                 .
          X        \\O/                                      |\\
          X.a##a.   M                                       |_\\
       .aa########a.>>                                    __|__
    .a################aa.                                 \\   /
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
""")

print("Welcome to Treasure Island. \nYour missin is to find the treasury.")
# use .lower() function to accept any case letters
select = input("  You're cross at a cross road. Where do you want to go? \n   Type \"left\" OR \"right\" \n").lower()
# check right or left
if select == "right":
    print("You fell into a hole. Game Over.")
elif select == "left":
    print("You've come to a lake. There is an island in the middle of the lake.")
    select = input("  Type \"wait\" to wait for a boat. Type \"swim\" to swim across. \n").lower()
    # check swim or wait
    if select == "swim":
        print("You get attacked by an angry trout. Game Over.")
    elif select == "wait":
        print("You arrive at the island unharmed. There is a house with 3 doors.")
        select = input("  One red, one yellow and one blue. Which colour do you choose? \n").lower()
        # check the colour
        if select == "red":
            print("Burned by fire. \nGame Over")
        elif select == "yellow":
            print("You Win!")
        elif select == "blue":
            print("Eaten by beasts \nGame Over")
        else:
            print("Wrong selection, Game Over!")
    else:
        print("Wrong selection, Game Over!")
else:
    print("Wrong selection, Game Over!")

