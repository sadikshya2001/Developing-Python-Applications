def BMIcalculation(weight, height):
    bmi = weight/ (height * height)
    return bmi

weight = float(input("Enter your weight in kilograms "))
height = float(input("Enter your height in meters "))
print("Your BMI is ",BMIcalculation(weight, height))