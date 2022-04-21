def canSum(targetSum,numbers):
    arr = [False for x in range(targetSum+1)]
    arr[0] = True
    for i in range(0,targetSum):
        print(i)
        print(arr)
        if(arr[i]==True):
            print(i)
            for number in range(len(numbers)):
                if i+number <= targetSum:
                    arr[i+number]=True
    print(arr)


canSum(7,[5,3,4])