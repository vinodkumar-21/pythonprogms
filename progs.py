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
def print_non_repeating(string):
    non_repeating = []
    for char in string:
        if string.count(char) == 1:
            non_repeating.append(char)
    print(non_repeating)

print_non_repeating('hello world')

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


# prog to count records by status from a list of dict
records = [
	{"id":1,"status":"open"},
	{"id":2,"status":"close"},
	{"id":3,"status":"open"},
]

status_count = []
for record  in records:
	status = record['status']
	status_count["status"]=status_count.get(status,0) + 1

print(status_count)

# prog to merge two sorted lists into a single sorted list
a = [1, 2, 5]
b = [0, 2, 4, 6]

result = sorted(a + b)
print(result)

# prog to merge two sorted lists into a single sorted list
a = [1, 2, 5]
b = [0, 2, 4, 6]

i = j = 0
result = []

while i < len(a) and j < len(b):
    if a[i] <= b[j]:
        result.append(a[i])
        i += 1
    else:
        result.append(b[j])
        j += 1

result.extend(a[i:])
result.extend(b[j:])

print(result)

# prog to find missing numbers in a list
lst = [4, 5, 3, 2, 6, 8]

result = []

for i in range(1,max(lst)+1):
	if i not in lst:
		result.append(i)
print(result)

# prog to add zeroes to the end of a list
lst = [0,2,"abc",3.4,0,2,"dgf"]
non_zero = []
zero_count = 0
for i in lst:
	if i == 0:
		zero_count +=1
	else:
		non_zero.append(i)
non_zero.extend([0]*zero_count)

print(non_zero)