def sumOfDigit(n, val):

    if (n < 10):
        val = val + n
        return val

    return sumOfDigit(n // 10, (n % 10) + val)

  
if __name__ == "main":
    num = 12345

    result = sumOfDigit(num, 0)

    print(result)
