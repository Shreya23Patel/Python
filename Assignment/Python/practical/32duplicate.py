n = int(input("Enter number of elements: "))

numbers = []

for i in range(n):
    num = int(input("Enter element: "))
    numbers.append(num)

new_list = []

for num in numbers:
    if num not in new_list:
        new_list.append(num)

print("List after removing duplicates:", new_list)
