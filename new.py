t=int(input())
import math
def test_prime(n):
    if (n==1):
        return False
    elif (n==2):
        return True
    else:
        for x in range(2,n):
            if(n % x==0):
                return False
        return True   
def calc(x):
    count=0
    for j in range(1,x+1):
        if(math.gcd(j,x)==j):
            count=count+1
    return count
for i in range(t):
    ans=0
    l=int(input())
    r=int(input())
    for j in range(l,r+1):
        if test_prime(calc(j)):
            ans=ans+1
    print(ans)