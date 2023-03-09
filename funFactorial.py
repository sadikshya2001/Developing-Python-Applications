def findingFactorial(number):
    factorial = 1
    for i in range(1, number + 1):
        factorial = factorial * i
    return factorial

number = int(input("Enter a number: "))
print("The factorial of the given number is", findingFactorial(number))