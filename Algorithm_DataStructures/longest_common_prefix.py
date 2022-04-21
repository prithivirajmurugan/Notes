def longestCommonPrefix(strs):
        longCommonPrefix = ""
        if(strs==None or len(strs)==0):
            return longCommonPrefix
        index = 0
        for i in strs[0]:
            for j in range(1,len(strs)):
                print(strs[j])
                print(strs[j][index],i)
                if(index >= len(strs[j]) or strs[j][index]!=i):
                    print("In If-condition")
                    return longCommonPrefix
                
            longCommonPrefix += i
            index+=1
        return longCommonPrefix

strs = ["flower","flow","flight"]
print(longestCommonPrefix(strs))