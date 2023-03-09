# print(3x^3 - 4x^2 + 9x +5 = 0)

#equation: 3x^3 - 2x^2 + 4x -7 = 0

x = -5.0

y = 0.0

while True:

    y = 3*x**3 - 4*x**2 + 9*x +5

    if y > -0.001 and y < 0.001:

        break

    x += 0.0001

print(x)

print(y)