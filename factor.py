def find_factors(n):
    factors=[]
    for i in range(1,n/2+1):
        if(n%i==0):
            factors.append(i)
    factors.append(n)
    return factors

n=10
factors=(find_factors(n))
print(factors)
