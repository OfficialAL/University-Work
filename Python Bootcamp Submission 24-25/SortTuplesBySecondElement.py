def Sort_Tuple(tup):
    tup.sort(key = lambda x: x[1]) 
    return tup

tup = [('rishav', 10), ('akash', 5), ('ram', 20), ('gaurav', 15)] 

print(Sort_Tuple(tup))
