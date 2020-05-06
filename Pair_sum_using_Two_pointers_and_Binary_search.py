L = [1,2,3,4,5,6]
front=0
rear=len(L)-1
tar=7
sum=0
L=sorted(L)

for i in range(len(L)):
    sum=L[front]+L[rear]
    if rear - front <= 0:
        break
    if sum == tar:
        print(L[front],"+",L[rear])
        front+=1
        rear-=1
    elif sum < tar:
        front+=1
    elif sum > tar:
        rear -= 1
