import math  #to calcuate square root the limit

def prime_sieve(n,sqrt):

    for e in range(2,sqrt+1):   #looping from 2 till square root of limit
        for i in range(e,n+1):   #looping from current iteration to limit
            c=i*e                 # Calculating the product of current element till limit
            if c > n:              # If product reaches beyond limit then
                break                #breaking the current element iteration
            else:
                L[c]=False   # Else setting the True Flag to False of the product elements

    for num in range(2, n+1):  # Looping from 2 till limit
        if L[num] == True:     # If the Flag is True
            prime_List.append(num)
    print(prime_List)

prime_List=[]
n= 200          # limit
sqrt=int(math.sqrt(n))    # calling function
L=[True for i in range(n+1)]   #Generating a list and assigning True to all the elements at first
prime_sieve(n,sqrt)   # calling function