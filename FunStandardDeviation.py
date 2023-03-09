def calculate_std_dev(numbers):
    n = len(numbers)
    mean = sum(numbers) / n
    variance = sum((x - mean) ** 2 for x in numbers) / (n - 1)
    std_dev = variance ** 0.5
    return std_dev

my_data = [1, 2, 3, 4, 5]
std_dev = calculate_std_dev(my_data)
print("Standard deviation:", std_dev)
