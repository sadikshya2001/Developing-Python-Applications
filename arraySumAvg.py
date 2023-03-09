import random

L = []
for _ in range(30):
    L.append(random.randint(0, 51))
print(L)
 
# variable to store the sum of
# the list
count = 0
 
# Finding the sum
for i in L:
    count += i
 
# divide the total elements by
# number of elements
avg = count/len(L)
 
print("sum = ", count)
print("average = ", avg)