from random import randint

count1 = 0
count2 = 0
count3 = 0
count4 = 0
count5 = 0
count6 = 0

for i in range(0, 101):
    dice = randint(1,7)

    if(dice == 1):
        count1 += 1
    if(dice == 1):
        count2 += 1
    if(dice == 1):
        count3 += 1
    if(dice == 1):
        count4 += 1
    if(dice == 1):
        count5 += 1
    if(dice == 1):
        count6 += 1

print("The dice had 1, 2, 3, 4, 5, 6 repeated for ", count1, count2, count3, count4, count5, count6, " times.")