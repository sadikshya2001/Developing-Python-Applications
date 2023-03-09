def average(x, y, z, a):
    return (x + y + z + a)/4

x = float(input("Enter float number 1: "))
y = float(input("Enter float number 2: "))
z = float(input("Enter float number 3: "))
a = float(input("Enter float number 4: "))

print("The average number of all the four numbers is ", average(x, y, z, a))