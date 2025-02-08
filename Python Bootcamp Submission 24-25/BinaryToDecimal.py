def binary_to_decimal(binary_str):
    return int(binary_str, 2)

def decimal_to_binary(decimal_num):
    return bin(decimal_num).replace("0b", "")

# Example usage
n = 4
binary = format(n, 'b')
print(binary)  # Output: '100'
binary = '100'
decimal = int(binary, 2)
print(decimal)  # Output: 4
