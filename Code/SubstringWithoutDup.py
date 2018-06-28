def topDown(li,inds,inde,m):

    if inde==len(li):
        return m

    if li[inde] in li[inds:inde]:
        prev=len(li[inds:inde])
        # print("prev inds",inds,li[inds:inde])
        inds+=li[inds:inde].index(li[inde])+1
        # print(inds,inde,prev,li[inds:inde])
        return topDown(li,inds,inde+1,max(m,prev))
    else:
        return topDown(li,inds,inde+1,m)

li=input()
print(topDown(li,0,1,1))
