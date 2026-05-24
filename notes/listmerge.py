#there is many types of merging list
list1 = [1,3,4,5]
list2 = [9,8,7,6]

# result = list1 + list2
# print(result)

# list1.extend(list2)
# print(list1)

# result3 = [*list1, *list2]
# print(result3)\

# for item in list2:
#     list1.append(item)
# print(list1)

result4 = list(set(list1 + list2))
print(result4)