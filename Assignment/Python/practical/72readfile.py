file = open("sample.txt", "w")
file.write("Hello Python\n")
file.write("This is a sample text file.\n")
file.write("File handling is easy.")
file.close()

# Read the entire file
file = open("sample.txt", "r")
content = file.read()
print(content)
file.close()
