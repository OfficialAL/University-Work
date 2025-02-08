def custom_sort(data, key_function):
    return sorted(data, key=key_function)

# Example usage
data = [{'age': 25}, {'age': 20}, {'age': 30}]
sorted_data = custom_sort(data, lambda x: x['age'])
print(sorted_data)  # Output should be: [{'age': 20}, {'age': 25}, {'age': 30}]
