
data = [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]


list1, list2 = zip(*data)


list1 = list(list1)
list2 = list(list2)

print("First list:", list1)
print("Second list:", list2)
