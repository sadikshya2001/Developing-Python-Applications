def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def combinations(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))

n = int(input("Enter the number: "))
k = int(input("Enter the choosing number: "))
result = combinations(n, k)
print(result)
