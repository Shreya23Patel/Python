start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

square_list = []

for i in range(start, end + 1):
    square_list.append(i * i)

print("Square list:", square_list)

print("First 5 elements:", square_list[:5])
print("Last 5 elements:", square_list[-5:])
