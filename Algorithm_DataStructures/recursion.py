def sum(numbers):
    total = 0
    for number in numbers:
        total += number
    return total


print(sum([1, 2, 4, 9]))


def sum_recursive(numbers):
    if numbers==[]:
        return 0
    return numbers[0] + sum_recursive(numbers[1:])

print(sum_recursive([1, 2, 4, 9]))