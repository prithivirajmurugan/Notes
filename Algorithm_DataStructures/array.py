new_list = [1, 2, 3]
# Accessing the elements
result = new_list[0]
print(result)

# Searching the elements
if 1 in new_list:
    print(True)

for n in new_list:
    if n == 1:
        print(True)
        break

# Appending
numbers = []
numbers.append(2)
numbers.append(200)
for i in range(0, len(numbers)):
    print(i)

# extend operation
numbers = []
numbers.extend([1, 2, 3])
for i in range(0, len(numbers)):
    print(i)
