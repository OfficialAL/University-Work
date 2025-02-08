import pandas as pd

print(pd.__version__)

df = pd.DataFrame({'X': [0, 1, 2], 'Y': [3, 4, 5]}, index=['A', 'B', 'C'])
print(df, end='\n\n')
#    X  Y
# A  0  3
# B  1  4
# C  2  5

print(df.T)
#    A  B  C
# X  0  1  2
# Y  3  4  5
