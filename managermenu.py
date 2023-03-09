totalbalance = 1000

answer = input("You want to deposit or withdraw money: ")

if answer.lower() == "deposit":
    deposit = int(input("Enter the amount: "))
    totalbalance = totalbalance + deposit
    print(deposit, "sum has been deposted to your account and your totalbalance is now", totalbalance)

elif answer.lower() == "withdraw":
    withdraw = int(input("Enter the amount: "))                                                                            
    if (withdraw < totalbalance):
        totalbalance = totalbalance - withdraw
        print(withdraw, "amount has been deducted and now you have", totalbalance)
    else:
        print("You dont have enough money")