my_list = ["Apple", "Banana", "Mango", "Orange"]

file = open("list.txt", "w")

for item in my_list:
    file.write(item + "\n")

file.close()

print("List written to file successfully.")
