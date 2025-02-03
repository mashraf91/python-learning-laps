"""
Calculate BMI (Body Mass Index)
bmi equation = weight / (height ** 2)
"""

weight = float(input("what's your weight? "))
height = float(input("what's your height? "))
bmi = weight / (height ** 2)

if bmi < 18.5:
    print("underweight")
elif bmi < 25:
    print("normal weight")
else:
    print("overweight")