def topDown(str1,str2,i,j):
    if i==len(str1) and j==len(str2):
        return 0
    if i==len(str1):
        return topDown(str1,str2,i,j+1)+1
    if j==len(str2):
        return topDown(str1,str2,i+1,j)+1

    if str1[i]==str2[j]:
        return topDown(str1,str2,i+1,j+1)+1

    return min(topDown(str1,str2,i+1,j)+1,topDown(str1,str2,i,j+1)+1)




str1 = input()
str2 = input()
print(topDown(str1,str2,0,0))
