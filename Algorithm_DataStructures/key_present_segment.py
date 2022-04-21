def is_key_present(arr, key, segment):
    i = 0
    while i < len(arr):
        j = 0
        while j < segment:
            if arr[j] == key:
                break
            j+=1
        if j==segment:
            return False
        i+=segment
    if i==len(arr):
        return True
    j = i-segment
    while j<len(arr):
        if arr[j]==key:
            break
        j+=1
    if j==len(arr):
        return False
    return True

