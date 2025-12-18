import random


n = int(input("Enter number of elements in the list: "))
my_list = []

for i in range(n):
    item = input("Enter element: ")
    my_list.append(item)


random_item = random.choice(my_list)
print("Randomly selected item:", random_item)
