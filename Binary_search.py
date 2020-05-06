
def bin_search(l):
    print(l)
    low = 0
    high = len(l)-1
    while low <= high:
        mid = (low + high) // 2
        if l[mid] == key:
            return mid,1
        elif key > l[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return 0,-1

l=[9,88,23,44,2,6,-69,25]
l=sorted(l)
key= 6

indx,f=bin_search(l)
if f == 1:
    print("Element",key,"found","at index",indx)
else:
    print("Element",key,"not found !")
