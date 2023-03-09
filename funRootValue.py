def sqrt(n):
    if n < 0:
        raise ValueError("Cannot compute square root of a negative number")
    elif n == 0:
        return 0
    else:
        ex = n / 2
        while abs(n - ex**2) > 1e-6:
            ex = (ex + n / ex) / 2
        return ex

number = int(input("Enter a number: "))
result = sqrt(number)
print(result)




