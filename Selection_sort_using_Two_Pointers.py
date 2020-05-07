# Performing Selection sort using two pointers.
def selection_sort():
    f = 0       #Pointer front
    n = f + 1       #Pointer Next
    FLAG = 0
    while (n != len(L)):
        min = L[f]
        for e in L[f:]:
            if e < min:
                min = e
                FLAG = 1
        if FLAG == 1:
            temp = L[f]
            indx = L.index(min)
            L[f] = min
            L[indx] = temp
            f += 1
            n = f + 1
            FLAG = 0
        else:
            f += 1
            n = f + 1
    print(L)
L = [-8547,0,897,-11, 0, 2, -20, 6, 4, 8, -4, 9, 5, 15, -5]
selection_sort()