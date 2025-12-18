file = open("sample.txt", "a")
file.write("Python is easy to learn.\n")
file.close()

# Read and display file content
file = open("sample.txt", "r")
print(file.read())
file.close()
