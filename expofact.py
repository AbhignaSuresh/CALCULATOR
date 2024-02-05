def expo(a,b):
    prod = 1
    for i in range(b):
        prod = prod * a
    return prod
    
def fact(n):
    if(n==1 or n==0):
        return 1
    else:
        return n*fact(n-1)

