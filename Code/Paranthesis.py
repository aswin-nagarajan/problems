
def fun(open,rem,pair):
    # print(open,rem)
    if(open==pair):
        return 0
    if(rem==0):
        return 1
    if(open<0):
        return 0

    return fun(open-1,rem,pair)+fun(open+1,rem-1,pair)

def para(pair):
    return fun(1,pair-1,pair)+1

def bottom(pair):

    table = [[0 for n in range(pair+1)] for jk in range(pair+1)]

    for i in range(pair+1):
        table[i][0]=1

    for j in range(1,pair+1):
        for i in range(pair+1):
            if i==0:
                table[i][j]=table[i+1][j-1]
            elif i==pair:
                table[i][j]=0
            else:
                table[i][j]=table[i-1][j]+table[i+1][j-1]

    return table[0][pair]



n=int(input())
print(bottom(n))



