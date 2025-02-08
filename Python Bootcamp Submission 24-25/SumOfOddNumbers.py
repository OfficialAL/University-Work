def sum_of_odds(numbers):
    return sum(num for num in numbers if num % 2 != 0)

numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = sum_of_odds(numbers_list)
print("The sum of all odd numbers in the list is:", result)
