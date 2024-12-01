'''
    Implemented on 1-Dec-2024.
'''
nums = [-99,1000,7,12,0,9,11,3]
p,c = 0, 1
while c < len(nums):
    c_indx = c
    while nums[c] < nums[p] and c > 0:
        temp = nums[p]
        nums[p] = nums[c]
        nums[c] = temp
        c-=1
        p-=1
    c = c_indx + 1      # restoring to last known position.
    p = c - 1
print(nums)