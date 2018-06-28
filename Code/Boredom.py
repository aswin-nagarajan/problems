def topDown(myset,freq,ind):
    if ind==len(myset):
        return 0
    else:
        ele = myset[ind]
        return max(ele*freq[ele]+topDown(myset,freq,ind+freq[ele]+freq[ele+1]),topDown(myset,freq,ind+freq[ele]))

def bottomUp(myset,freq):
    tab = [0 for n in range(len(myset))]
    tab[-1]=myset[-1]*freq[myset[-1]]
    tab[-2]=max(myset[-2]*freq[myset[-2]],tab[-1])
    for i in range(len(myset)-3,-1,-1):
        tab[i]=max(myset[i]*freq[myset[i]]+tab[i+2],tab[i+1])

    print(tab)

    return(tab[0])





li = list(map(int,input().split()))
m = max(li)
freq=[]
for i in range(0,m+2):
    freq.append(li.count(i))
print(topDown(sorted(li),freq,0))
print(bottomUp(list(set(sorted(li))),freq))
