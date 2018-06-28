def topDown(arr,ind):
    if ind>=len(arr):
        return 0;
    return max(arr[ind]+topDown(arr,ind+2),topDown(arr,ind+1))

li=list(map(int,input().split()))
print(topDown(li,0))
