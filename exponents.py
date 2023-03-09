base = float(input("Enter a base number: "))
exponent = int(input("Enter the exponent:"))
output = 1

for _ in range(abs(exponent)):
    output = output * base

if(exponent < 0):
    output = 1 / output

print("The output of the given number is", output)
