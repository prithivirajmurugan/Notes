def split(list):
    """
    Divide the unsorted list at midpoint into sublists
    Returns two sublists - left and right
    Takes overall O(log n)

    but it python slice takes O(k log n) operation
    """
    mid_point = len(list) // 2
    left = list[:mid_point]
    right = list[mid_point:]
    return left, right


def merge(left, right):
    """merges two lists (array), sorting them in the process
    Returns a new merged list

    Runs in overall O(n log n)
    """
    l = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            l.append(left[i])
            i += 1
        else:
            l.append(right[j])
            j += 1
    while i < len(left):
        l.append(left[i])
        i += 1
    while j < len(right):
        l.append(right[j])
        j += 1
    return l


def merge_sort(list):
    """
    Sort a list in ascending order
    Returns a new sorted list
    Divide: Find the midpoint of the list
    and divide into sublists

    Conquer: Recursively sort the sublists created in previous step
    Combine: Merge the sorted sublists created in previous step

    Overall take O(n logn)
    """
    if len(list) <= 1:
        return list
    left_half, right_half = split(list)  # Divide
    left = merge_sort(left_half)  # Recursive split
    right = merge_sort(right_half)  # Recursive split

    return merge(left, right)  # Conquer and Combine


numbers = [54, 25, 82, 28, 17, 41, 62, 53, 1, 0]
l = merge_sort(numbers)
print(l)


def verify_sorted(list):
    n = len(list)
    if n == 0 or n == 1:
        return True
    return list[0] < list[1] and verify_sorted(list[1:])


print(verify_sorted(l))
