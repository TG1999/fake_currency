from math import inf
def func(arr):
    available=list(arr)
    for ele in arr:
        if ele&1:
            available.append(ele<<1)
        else:
            x=ele
            while True:
                x >>= 1
                available.append(x)
                if x&1:
                    break
    available.sort()
    print(available)
    ans=inf
    for i in range(1,len(available)):
        ans=min(ans,abs(available[i]-available[i-1]))
    return ans
