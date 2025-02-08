test_keys = ["Alex", "Orlando", "Zack"]
test_values = [1, 4, 5]

print("Original key list is : " + str(test_keys))
print("Original value list is : " + str(test_values))

res = {test_keys[i]: test_values[i] for i in range(len(test_keys))}

print("Resultant dictionary is : " + str(res))
