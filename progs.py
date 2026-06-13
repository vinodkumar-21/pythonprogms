#program to find the smallest number in a list
lst = [1, 3, 4, 5, 6, 9, 8, 7, 5]
temp = lst[0]
print(len(lst))
for i in range(1, len(lst)):
    if lst[i] < temp:
        temp = lst[i]
print(temp)

# prog to find the largest number in a list
lst = [1, 3, 4, 5, 6, 9 , 8, 7, 5]
temp = lst[0]   
for i in range(1, len(lst)):
    if lst[i] > temp:
        temp = lst[i]
print(temp)

# prog to find the second largest number in a list
lst = [1, 3, 4, 5, 6, 9, 8, 7, 5]
temp1 = lst[0]  
temp2 = lst[0]
for i in range(1, len(lst)):
    if lst[i] > temp1:
        temp2 = temp1
        temp1 = lst[i]
    elif lst[i] > temp2 and lst[i] != temp1:
        temp2 = lst[i]
print(temp2)

# prog to find second largest number in a list
lst = [1, 3, 4, 5, 6, 9, 8, 7, 5]
second_largest = sorted(set(lst))[-2]
print(second_largest)

# prog to find the second smallest number in a list
lst = [1, 3, 4, 5, 6, 9, 8, 7, 5]
second_smallest = sorted(set(lst))[1]
print(second_smallest)

# prog to find the second smallest number in a list
lst = [1, 3, 4, 5, 6, 9, 8, 7, 5]
temp1 = lst[0]
temp2 = lst[0]
for i in range(1, len(lst)):
    if lst[i] < temp1:
        temp2 = temp1
        temp1 = lst[i]
    elif lst[i] < temp2 and lst[i] != temp1:
        temp2 = lst[i]
print(temp2)

# prog to find the sum of all numbers in a list
lst = [1, 3, 4, 5, 6, 9, 8, 7, 5]
total = 0
for i in lst:
    total += i
print(total)

# prog to find the average of all numbers in a list
lst = [1, 3, 4, 5, 6, 9, 8, 7, 5]   
total = sum(lst)
average = total / len(lst)
print(average)

# prog to swap the first and last elements of a list
lst = [1, 3, 4, 5, 6, 9 , 8, 7, 5]
temp = lst[0]
lst[0] = lst[-1]
lst[-1] = temp
print(lst)

# prog to reverse a list
lst = [1, 3, 4, 5, 6, 9, 8, 7, 5]
reversed_lst = lst[::-1]
print(reversed_lst)

# prog to find the frequency of each element in a list
lst = [1, 3, 4, 5, 6, 9, 8, 7, 5]
frequency = {}
for i in lst:
    if i in frequency:
        frequency[i] += 1
    else:
        frequency[i] = 1
print(frequency)

# prog to find the simple  list from nested list
lst = [1, 2, [3, 4], 5, [6, 7], 8, 9, [10, [11]]]

result = []
def flatten(lst):
    for i in lst:
        if isinstance(i, list):
            flatten(i)
        else:
            result.append(i)
flatten(lst)
print(result)

# progg to  make  dictt using one list as keys and another list as values
keys = ['a', 'b', 'c']
values = [1, 2, 3]
my_dict = dict(zip(keys, values))
print(my_dict)

# other way to make dict using one list as keys and another list as values
keys = ['a', 'b', 'c']
values = [1, 2, 3]
my_dict = {}
for i in range(len(keys)):
    my_dict[keys[i]] = values[i]
print(my_dict)

# prog for decorator function used
def update_data(func):
    def wrapper():
        print("this is before decorators")
        func()
        print("this is after decorator")
    return wrapper()

@update_data
def print_data():
    print("hey  this is mainn function")
print_data()

# prog to print all non repetitiong character
string = "hello world"
non_repeating = []

def print_non_repeating():
    for char in string:
        if string.count(char) == 1:
            non_repeating.append(char)
    print(non_repeating)

print_non_repeating()

# prog to reverse a list using recursion
lst = [1, 2, 3, 4, 5]
left = 0
right = len(lst) - 1

for i in lst:
    if left < right:
        lst[left], lst[right] = lst[right], lst[left]
        left += 1
        right -= 1
print(lst)