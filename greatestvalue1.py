num1 = 10
num2 = 12
num3 = 9

if (num1 >= num2) and (num1 >= num3):
    greatest = num1

elif (num2 >= num1) and (num2 >= num3):
    greatest = num2

else:
    greatest = num3

print('The biggest number is ', greatest)