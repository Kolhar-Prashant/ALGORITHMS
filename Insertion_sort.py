L=[0,6521,3,100000,4,-11,786,-85269,5,6,-1,0,-859]

for i in range(len(L)):  # Running a loop on list
    if i <= len(L)-2:      # current iteration is less than length
                                                         #of list - 2
        next=i+1		#incrementing pointer to next ele
    if L[next] < L[i]:    #if next ele is less than curr ele
        temp=L[next]        #storing in temp var

        while (temp < L[i] and i != -1):  #Now performing if any
                                       #element is less than curr ele
            piv_indx=i+1      #fetching addr of next ele
            L[piv_indx]=L[i]  #shifting element to right hand side
            i-=1               # counter to go backwards
        x=L.index(L[piv_indx-1])  #Finally inserting curr ele at
                                        #it’s right index
        L[x]=temp
print(L)
