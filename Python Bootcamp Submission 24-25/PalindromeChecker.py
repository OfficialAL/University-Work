def is_palindrome(s):
    s = ''.join(filter(str.isalnum, s)).lower()
    return s == s[::-1]

# Check input
s = input("Enter String to check if it is a Palindrome: ").strip()
ans = is_palindrome(s)
# Output
if ans:
    print("Yes, This is in fact a Palindrome")
else:
    print("No, This is not a Palindrome")
