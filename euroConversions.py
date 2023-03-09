amount = int(input("Enter your euro value: "))

bills = [500, 200, 100, 50, 20, 10, 5]

for bill in bills:
    count = amount // bill
    if count > 0:
        print(f"{count} times of {bill}")
        amount = amount % bill
