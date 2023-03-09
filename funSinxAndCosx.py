import math

def sin(x, n):
    sin_x = 0
    for i in range(n):
        sign = (-1) ** i
        numerator = x ** (2 * i + 1)
        denominator = math.factorial(2 * i + 1)
        sin_x += sign * numerator / denominator
    return sin_x

def cos_approx(x):
    x = math.radians(x)  
    cos_x = 0
    sign = 1
    for n in range(0, 10):
        term = sign * (x**(2*n)) / math.factorial(2*n)
        cos_x += term
        sign *= -1
    return cos_x

print(sin(120, 5))
print(cos_approx(120))

