print("Welcome to the tip calculator!")

# note that input() returns string data type
total_bill = float(input("What was the total bill? $ "))
tip_percentage = float(input("How much tip would you like to give? 10, 12, or 15? "))
number_of_people = float(input("How many people to split the bill? "))

# need to calculate how much person should pay with 2 dicimals
each_person = round((total_bill + ((tip_percentage * total_bill)/100)) / number_of_people, 2)

print(f"Each person should pay: ${each_person}")