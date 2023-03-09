side1 = float(input("Enter side 1 value: "))
side2 = float(input("Enter side 2 value: "))
side3 = float(input("Enter side 3 value: "))

if side1 == side2 and side1 == side3 and side2 == side3:
    print("It is an equilateral triangle.")

elif side1 == side2 or side1 == side3 or side2 == side3:
    print("It is an Isosceles Triangle")

else:
    print("It is a Scalene Triangle")
