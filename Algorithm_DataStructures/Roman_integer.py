def romanToInt(s: str) -> int:
        dic  = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        
        s = str(s)
        l = list(s)
        result = 0
        for i in range(0,len(l)):
            curr = l[i]
            print(curr)
            if i == 0:
                result = result + dic[curr]
            elif dic[l[i]] <= dic[l[i-1]]:
                result = result + dic[l[i]]
            else:
                result = result + abs(dic[l[i-1]] - dic[l[i]])-dic[l[i-1]]
        return result

print(romanToInt("IV"))