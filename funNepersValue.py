def approximation_e(n):
    e = 1
    fact = 1
    for i in range(1, n):
        fact *= i
        e += 1/fact
    return e

num = int(input("Enter a value: "))
print("The Nepers value is ", approximation_e(num))