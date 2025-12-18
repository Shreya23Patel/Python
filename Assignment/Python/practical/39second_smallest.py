
n = int(input("Enter number of elements: "))
numbers = []

for i in range(n):
    num = int(input("Enter number: "))
    numbers.append(num)


numbers.sort()


print("Second smallest number is:", numbers[1])
