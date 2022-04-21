import random
def get_maximum(arr):
    max = arr[0]
    for i in arr:
        if i>max:
            max=i
    return max

def get_minimum(arr):
    min = arr[0]
    for i in arr:
        if i<min:
            min=i
    return min


numbers = random.sample(range(10),10)
print(get_maximum(numbers))
print(get_minimum(numbers))