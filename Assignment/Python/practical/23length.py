s = input("Enter a string: ")

length = len(s)

if length < 2:
    print("")
else:
    first_two = s[0] + s[1]
    last_two = s[length - 2] + s[length - 1]
    print(first_two + last_two)
