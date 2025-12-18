
n = int(input("Enter number of key-value pairs: "))
my_dict = {}

for i in range(n):
    key = input(f"Enter key {i+1}: ")
    value = input(f"Enter value {i+1}: ")
    my_dict[key] = value

key_to_check = input("Enter key to check: ")


if key_to_check in my_dict:
    print(f"The key '{key_to_check}' exists in the dictionary.")
else:
    print(f"The key '{key_to_check}' does not exist in the dictionary.")
