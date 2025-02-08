def divisorSum( n ):
    sum = 0
    for i in range(1, n + 1):
        sum += int(n / i) * i
    return int(sum)
     
n = 4
print( divisorSum(n))
n = 5
print( divisorSum(n))
