def power(x, n):
    pow = 1
    for i in range(n):
        pow = pow * x
    return pow

if __name__ == 'main':
    x = 2
    n = 3
    print(power(x, n))
