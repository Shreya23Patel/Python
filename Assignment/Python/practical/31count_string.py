n = int(input("Enter number of strings: "))

strings = []

for i in range(n):
    s = input("Enter string: ")
    strings.append(s)

count = 0

for s in strings:
    if len(s) >= 2 and s[0] == s[-1]:
        count += 1

print("Number of matching strings:", count)
