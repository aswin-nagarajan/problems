def edit(src,dest,ind):

    print(src,dest,ind)

    if ind==len(dest):
        return 0

    if len(src)>len(dest):
        if ind==len(dest):
            num= len(src)-len(dest)
            return num
    elif len(dest)>len(src):
        if ind==len(src):
            num= len(dest)-len(src)
            return num

    if src[ind]==dest[ind]:
        return edit(src,dest,ind+1)

    else:
        print("in for ind ",ind)

        dele = src[:]
        dele.pop(ind)
        repl = src[:]
        repl[ind]=dest[ind]
        if(len(dest)>len(src)):
            temp = src[:ind]
            temp.append(dest[ind])
            ins = temp+src[ind:]
        else:
            ins =repl[:]


        print(ins,dele,repl)
        return min(edit(ins,dest,ind+1)+1,edit(dele,dest,ind)+1,edit(repl,dest,ind+1)+1)


def memoize(src,dest,ind,tab):
    if tab[ind]==0:

        print(src,dest,ind,tab)

        if ind==len(dest):
            return 0

        if len(src)>len(dest):
            if ind==len(dest):
                tab[ind]= len(src)-len(dest)
                return tab[ind]
        elif len(dest)>len(src):
            if ind==len(src):
                tab[ind]= len(dest)-len(src)
                return tab[ind]

        if src[ind]==dest[ind]:
            tab[ind] = memoize(src,dest,ind+1,tab)
            return tab[ind]

        else:
            print("in for ind ",ind)

            dele = src[:]
            dele.pop(ind)
            repl = src[:]
            repl[ind]=dest[ind]
            if(len(dest)>len(src)):
                temp = src[:ind]
                temp.append(dest[ind])
                ins = temp+src[ind:]
            else:
                ins =repl[:]


            # print(ins,dele,repl)
            tab[ind] = min(memoize(ins,dest,ind+1,tab)+1,memoize(dele,dest,ind,tab)+1,memoize(repl,dest,ind+1,tab)+1)
            return tab[ind]

    else:
        return tab[ind]


def topDown(i,j,src,dest,tab):

    print(i,j)

    if i==len(src) or j==len(dest):
        return 0



    if tab[i][j]==0:
        if src[i]==dest[j]:
            tab[i][j] = topDown(i+1,j+1,src,dest,tab)

        else:
            tab[i][j] = min(topDown(i+1,j,src,dest,tab)+1,topDown(i,j+1,src,dest,tab)+1,topDown(i+1,j+1,src,dest,tab)+1)

    return tab[i][j]

li = [0 for i in range(len("vishal")+1)]

src="apiskal"
dest = "vishal"

tab = [[0 for i in range(len(src)+1)] for j in range(len(dest)+1)]

print(topDown(0,0,list(src),list(dest),tab))
print(tab)
