
n = int(input("Enter number of elements in the list: "))
my_list = []

for i in range(n):
    item = input("Enter element: ")
    my_list.append(item)


if n < 3:  
    print("Not enough elements to split into variables")
else:
    a, b, c, d = my_list[:4]  
    print("Variable a:", a)
    print("Variable b:", b)
    print("Variable c:", c)
    print("variable d:", d)
    