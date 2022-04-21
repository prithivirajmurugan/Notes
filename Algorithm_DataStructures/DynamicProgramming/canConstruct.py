"""
Write a function `canConstruct(target,workBank)` that accepts a target string
and an array of strings.

The function should return a boolean indication whether or not the  `target`
can be constructed by concatenating elements of the  `wordBank` array

You may reuse elements of `wordBank` as many times as needed

"""

def canConstruct(target,workbank,memo=[], idx=0):

    pos = target.find(workbank[idx])
    if pos != -1:
        memo.append(True)
        idx += 1
        try:
            suffix = target[len(workbank[idx]):]
            canConstruct(suffix,workbank,memo, idx)
        except IndexError: # Here we exit the recursive call
            pass
    else: # In case it did not find string, append False 
        memo.append(False)
        
    return all(memo) # in order to be True, all item in memo must be True

def canConstruct(target,wordBank,memo=None):
    if memo == None:
        memo = {}
    if target == '':
        return True
    if target in memo:
        return memo[target]
    for word in wordBank:
        size = len(word)
        prefix_target = word[:size]
        if (word==prefix_target):
            remaining_target = target[size:]
            if canConstruct(remaining_target,wordBank,memo):
                memo[remaining_target] = True
                return memo[remaining_target]
    memo[target] = False
    return memo[target]


print(canConstruct('abcdef',['ab','abc','cd','def','abcd']))
print(canConstruct("abababab",["ab"]))
print(canConstruct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef',
['e',
'ee',
'eee',
'eeee',
'eeeee',
'eeeeee',
'eeeeeee']))

