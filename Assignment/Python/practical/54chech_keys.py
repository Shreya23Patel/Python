
n = int(input("Enter number of key-value pairs: "))
my_dict = {}

for i in range(n):
    key = input("Enter key: ")
    value = input("Enter value: ")
    my_dict[key] = value

keys = input("Enter keys to check (separated by space): ").split()

for key in keys:
    if key not in my_dict:
        print("All keys do NOT exist in the dictionary.")
        break
else:
    print("All keys exist in the dictionary.")

print("Dictionary:", my_dict)
