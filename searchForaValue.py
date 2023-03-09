def search_array(arr, value):
    for i in range(len(arr)):
        if arr[i] == value:
            return i
    return -1

# Example usage
my_arr = [1, 2, 3, 4, 5]
search_value = 3
result = search_array(my_arr, search_value)
if result == -1:
    print(f"{search_value} not found in array")
else:
    print(f"{search_value} found at index {result}")
