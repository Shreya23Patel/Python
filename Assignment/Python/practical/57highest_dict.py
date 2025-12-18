
n = int(input("Enter number of elements: "))
d = {}

for i in range(n):
    key = input("Enter key: ")
    value = int(input("Enter value: "))
    d[key] = value


values = list(d.values())
values.sort(reverse=True)


print("Highest 3 values are:")
for i in range(3):
    print(values[i])
