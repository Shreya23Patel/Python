n = int(input("Enter number of characters: "))

char_list = []

for i in range(n):
    ch = input("Enter character: ")
    char_list.append(ch)

result = ""

for ch in char_list:
    result += ch

print("Converted string:", result)
