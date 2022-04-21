import random

def count_pair_sum(values,sum):
    map_elements = [0]*1000
    twice_count = 0
    n = len(values)
    for i in range(0,n):
        map_elements[values[i]]+=1
    for i in range(0,n):
        twice_count +=map_elements[sum-values[i]]
        if(sum - values[i]==values[i]):
            twice_count -= 1
    return int(twice_count/2)