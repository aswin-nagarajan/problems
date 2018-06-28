def topDown(li,s,e,ch):
    if s==e:
        if ch%2==0:
            return li[s]
        else:
            return 0
    else:
        if ch%2==0:
            temp1 = topDown(li,s+1,e,ch+1)
            temp2 = topDown(li,s,e-1,ch+1)
            if temp1<temp2:
                return temp1+li[s]
            elif temp2<temp2:
                return temp2+li[e]
            else:
                return temp1+max(li[s],li[e])
        else:
            return min(topDown(li,s+1,e,ch+1),topDown(li,s,e-1,ch+1))


li=list(map(int,input().split()))

print(topDown(li,0,len(li)-1,0))
