# Calculating Maximum subarray sum using Kadane's Algorithm.
def Kadane_Max_subarray_sum():
    curr_sum=0
    max_sum=0
    temp=0
    for e in L:
        temp=curr_sum
        curr_sum+=e
        if curr_sum < 0:
            curr_sum=0
            continue
        if temp > curr_sum:
            if temp > max_sum:
                max_sum=temp
        else:
            if curr_sum > max_sum:
                max_sum=curr_sum
    print("Maximum subarray sum :",max_sum)

L=[-4,1,3,-2,6,2,-1,-4,-7]
Kadane_Max_subarray_sum()

