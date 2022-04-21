def sort012(arr,n):
    count0=0
    count1=0
    count2=0
    for i in range(0,n):
        if (arr[i]==0):
            count0=count0+1
        if(arr[i]==1):
            count1=count1+1
        if(arr[i]==2):
            count2=count2+1
    return [].extend([0]*count0).extend([1]*count1).extend([2]*count2)