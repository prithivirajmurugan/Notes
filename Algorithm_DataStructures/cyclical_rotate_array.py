import random
def cyclical_rotate_array(values,k):
    n = len(values)
    rotated_array = []
    j=k
    while(j<n):
        rotated_array.append(values[j])
        j+=1
    j=0
    while j<k:
        rotated_array.append(values[j])
        j+=1
    return rotated_array

numbers = random.sample(range(10),10)
print(numbers)
rotated_array = cyclical_rotate_array(numbers,3)
print(rotated_array)

def rotate(arr,n):
    x = arr[n-1]
    for i in range(n-1,0,-1):
        arr[i]=arr[i-1]
    arr[0] = x