weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in m: "))

bmi = weight / (height * height)

if bmi < 18.5:
    print("Your BMI value is " , bmi , " and it is underweight.") 

elif bmi >= 18.5 and bmi < 24.9:
    print("Your BMI value is ", bmi , " and it is healthy.")

elif bmi >= 24.9 and bmi < 30:
    print("Your BMI value is ", bmi , " and it is overweight.")

else:
    print("Your BMI value is ", bmi , " and it is obesity.")
