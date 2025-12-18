a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a == b or b == c or a == c:
    sum = 0
else:
    sum = a + b + c

print("The sum is:", sum)
