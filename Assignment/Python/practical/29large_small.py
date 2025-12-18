n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))


total = n1 + n2
print("Sum =", total)


if n1 == n2:
    print("Both numbers are equal")

elif n1 > n2:
    print(n1, "is greater")

else:
    print(n2, "is greater")
