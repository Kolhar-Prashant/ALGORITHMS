
def calc(n,tar):
    sum=0
    indx=[]
    for e in L:
        sum = n+e
        if sum == tar:
            if n not in l_cache and e not  in l_cache:
                print("Sum found", n, "+", e, "equals",tar)
                l_cache.append(n)
                l_cache.append(e)

L=[-1, 5,15, 4, 13, 7, -4, 10, 1, 6, 8]
l_cache=[]                      #memoziation concept.
print(L)
x=[]
tar=21

for e in L:
    calc(e,tar)
