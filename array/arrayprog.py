#Find duplicates

arr = [1,2,2,1,3,4]
dup = []

for i in arr:
    if i not in dup:
        dup.append(i)
print(dup)


#remove duplicate
list = [1, 2, 2, 3]

result = []

for i in list:
    if i not in result:
        result.append(i)

print(result)



# Write a Python program to find numbers that are greater than 10 and have odd first and last digits.
# Input:
# [1, 3, 79, 10, 4, 1, 39]
# Output:
# [79, 39]
# Input:
# [11, 31, 77, 93, 48, 1, 57]
# Output:
# [11, 31, 77, 93, 57]


nums = [1, 3, 79, 10, 4, 39, 62]

nums = [11, 31, 77, 93, 48, 1, 57]
result = []
for num in nums:
    if num > 10:
        digit1 = int(str(num)[0])
        digit2 = int(str(num)[-1])
        
        if digit1 % 2 != 0 and digit2 % 2 != 0:
            result.append(num)
print(result)


