def common_member(list1, list2):
    for item in list1:
        if item in list2:
            return True
    return False

n1 = int(input("Enter number of elements in first list: "))
list1 = []

for i in range(n1):
    val = input("Enter element: ")
    list1.append(val)

n2 = int(input("Enter number of elements in second list: "))
list2 = []

for i in range(n2):
    val = input("Enter element: ")
    list2.append(val)

# Function call
result = common_member(list1, list2)

print("Common member exists:", result)
