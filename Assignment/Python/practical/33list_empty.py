n = int(input("Enter number of elements in the list: "))

my_list = []

for i in range(n):
    item = input("Enter element: ")
    my_list.append(item)

if not my_list:
    print("The list is empty")
else:
    print("The list is not empty")
    print("List elements:", my_list)
