def selection_sort():
    f = 0
    n = f + 1
    FLAG = 0

    while (n != len(L)):
        min = L[f]
        print(L[f], L[n])

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

L = [-11, 0, 2, -20, 6, 4, 8, -4, 9, 5, 15, -5]
selection_sort()