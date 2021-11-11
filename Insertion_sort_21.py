L = [2000,-111,14,-2,22,-1,5500,3,-98,1000,21,13,-2000]
indx = 1       # starting from 1st ele.
while indx != len(L):
    c = indx     # taking curr_indx.
    temp = L[c]   # storing curr_indx value in temp.
    c-=1            # loop starting from curr_indx-1.
    while c != -1:   # looping till curr_indx doesn't reach 0th pos.
        if temp < L[c]:   # if less ? then 
            L[c+1] = L[c]   # Shifting value one pos ahead.
        else:
            break         # breaking if curr_value is less than temp.
        c-=1            # decr curr_indx.
    L[c+1] = temp     # assiging temp to it's correct indx in asc ord. 
    indx+=1         # incr indx.
print(L)