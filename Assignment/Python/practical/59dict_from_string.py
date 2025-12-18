string = input("Enter a string: ")
count = {}

for ch in string:
    if ch in count:
        count[ch] = count[ch] + 1
    else:
        count[ch] = 1

print("Character count dictionary:", count)
