
n = int(input("Enter number of elements for the tuple: "))
my_tuple = []

for i in range(n):
    item = input("Enter element: ")
    my_tuple.append(item)  


my_tuple = tuple(my_tuple)

print("Tuple with different data types:", my_tuple)
