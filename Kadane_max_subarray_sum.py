def Kadane(L):
   ms=0
   cs=0
   for e in L:
       sum = cs + e
       if sum < 0:
           cs=0
       else:
           cs=sum
       if cs > ms:
           ms=cs
   print("Max sum :",ms)
L=[-4,1,3,-2,6,2,-1,-4,-7] #provide array values here.
Kadane(L)