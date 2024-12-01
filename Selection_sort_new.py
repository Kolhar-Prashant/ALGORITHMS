'''
    Logic: prev is set to 0 and curr to 1. Checking if there is smaller element compared with prev in current iteration.
            if smaller element is found then swapping it till prev.
            In next iteration incrementing prev + 1 and curr + 1 and again performing same process once curr reaches len of nums.
'''

nums = [-1,7,12,0,4,14,-11]
prev, curr = 0, 1

while curr != len(nums):
    last_indx = curr
    found = 0
    mi = nums[prev]
    while curr < len(nums):
        if nums[curr] < nums[prev] and nums[curr] < mi:
            mi = nums[curr]
            shortest_indx = curr
            found = 1
        curr += 1
    if found == 1:
        curr = shortest_indx
        while curr != prev:
            temp = nums[curr-1]
            nums[curr-1] = nums[curr]
            nums[curr] = temp
            curr -= 1
    curr = last_indx + 1
    prev = curr - 1
print(nums)




'''while indx != len(nums)-1:
    c_indx = indx
    found = 0
    mi = max(nums)
    while indx <= len(nums)-1:
        if nums[indx] < nums[curr] and nums[indx] < mi:
            mi = nums[indx]
            shortest_indx = indx
            found = 1
        indx += 1
    if found == 1:
        indx = shortest_indx
        while indx != curr:
            temp = nums[indx-1]
            nums[indx-1] = nums[indx]
            nums[indx] = temp
            indx-=1
    indx = c_indx + 1
    curr = indx + 1
print(nums)

'''