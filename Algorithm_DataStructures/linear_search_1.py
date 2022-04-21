def index_of_item(collection,target):
    for i in range(0,len(collection)):
        if target==collection[i]:
            return i
