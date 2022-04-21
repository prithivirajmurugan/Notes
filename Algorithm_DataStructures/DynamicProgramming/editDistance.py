def editDistance(str1,str2):
    if str1 is None or str1==[]:
        return len(str2)
    if str2 is None or str2==[]:
        return len(str1)
    if (str1==str2):
        return editDistance(str1[1:],str2[1:])
    d = editDistance(str1[1:],str2)
    u = editDistance(str1[1:],str2[1:])
    i = editDistance(str1,str2[1:])

    return min(u,d,i)

print(editDistance("Hello","Hallo"))