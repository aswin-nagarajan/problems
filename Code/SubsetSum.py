def topDown(arr,ind,s):

    if s==0:
        return True

    if ind==len(arr):
        return False



    return topDown(arr,ind+1,s-arr[ind]) or topDown(arr,ind+1,s)

def another(arr,ind,s):
    if s==0:
        return 1
    if ind==len(arr):
        return 0

    return another(arr,ind+1,s-arr[ind])+another(arr,ind+1,s)

s=int(input())
li = list(map(int,input().split()))
print(another(li,0,s))
