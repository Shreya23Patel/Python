
n = int(input("Enter number of elements in the list: "))
numbers = []

for i in range(n):
    num = input("Enter element: ")
    numbers.append(num)


unique_list = []
for item in numbers:
    if item not in unique_list:
        unique_list.append(item)

print("List of unique values:", unique_list)
