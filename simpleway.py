# prog no to move all leading zeros to the end of a list
def leading_zero_end(lst):
    non_zero = []
    zero_count = 0
    for i in lst:
        if i == 0:
            zero_count += 1
        else:
            non_zero.append(i)
    return non_zero + [0] * zero_count
print(leading_zero_end([0, 2, "abc", 3.4, 0, 2, "dgf"]))

# prog to find the missing numbers in a list
def find_missing_numbers(lst):
    result = []
    for i in range(1, max(lst) + 1):
        if i not in lst:
            result.append(i)
    return result
print(find_missing_numbers([4, 5, 3, 2, 6, 8]))

# prog to merge two sorted lists into a single sorted list
def merge_sorted_lists(a, b):
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
    return result
print(merge_sorted_lists([1, 3, 5], [2, 4, 6])) 

# prog to count the occurrences of each status in a list of records
def count_status(records):
    status_count = {}
    for record in records:
        status = record['status']
        status_count[status] = status_count.get(status, 0) + 1
    return status_count
records = [
	{"id":1,"status":"open"},
	{"id":2,"status":"close"},
	{"id":3,"status":"open"},
]
print(count_status(records))

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

# prog to print all non repetitiong character
string = "hello world"
non_repeating = []
def print_non_repeating():
    for char in string:
        if string.count(char) == 1:
            non_repeating.append(char)
    print(non_repeating)

print_non_repeating()

# prog to find the frequency of each element in a list
lst = [1, 3, 4, 5, 6, 9, 8, 7, 5]
frequency = {}
for i in lst:
    if i in frequency:
        frequency[i] += 1
    else:
        frequency[i] = 1
print(frequency)

# prog to find the longest substring without repeating characters and length of the longest substring
def longest_substring(str):
    start = 0
    max_length = 0
    char_index = {}
    longest_substr = ""
    
    for end in range(len(str)):
        if str[end] in char_index and char_index[str[end]] >= start:
            start = char_index[str[end]] + 1
        
        char_index[str[end]] = end
        current_length = end - start + 1
        
        if current_length > max_length:
            max_length = current_length
            longest_substr = str[start:end + 1]
    
    return longest_substr, max_length
print(longest_substring("abcabcbb"))  # Output: ('abc', 3)