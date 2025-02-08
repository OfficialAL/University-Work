def find_second_largest(numbers):
    largest = second_largest = float('-inf')
    
    for num in numbers:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num
    
    return second_largest

numbers = [10, 20, 4, 45, 99]
second_largest = find_second_largest(numbers)
print("The second largest number is:", second_largest)
