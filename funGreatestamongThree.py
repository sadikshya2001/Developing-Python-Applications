
def findingGreatestNumber(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        print("The greatest number is ", num1)
    elif num2 > num1 and num2 > num3:
        print("The greatest number is ", num2)
    else:
        print("The greatest number is ", num3)

num1 = 10
num2 = 12
num3 = 9
findingGreatestNumber(num1, num2, num3)
