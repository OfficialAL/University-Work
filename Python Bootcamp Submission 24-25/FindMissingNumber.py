# Find Missing Number puzzle

def find_missing_number(arr, n):
    full_set = set(range(1, n + 1))
    arr_set = set(arr)
    return list(full_set - arr_set)

# Example usage
a = [1, 3, 4, 5, 7, 8, 9, 10]
b = [x for x in range(a[0], a[-1] + 1)]
a = set(a)
print(list(a ^ set(b)))  # Output: [2, 6]
