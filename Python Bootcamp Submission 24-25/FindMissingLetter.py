f=lambda a,*r:r[0]-a>1and chr(a+1)or f(*r)

print(f(*b'ABD'))
