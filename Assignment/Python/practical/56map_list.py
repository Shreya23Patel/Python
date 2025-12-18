
n = int(input("Enter number of elements: "))
list1 = []
list2 = []

print("Enter elements for first list (keys):")
for i in range(n):
    list1.append(input())

print("Enter elements for second list (values):")
for i in range(n):
    list2.append(int(input()))

# Create dictionary
result = {}

for i in range(n):
    result[list1[i]] = list2[i]

print("Mapped Dictionary:", result)
