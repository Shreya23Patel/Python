file = open("read.txt", "w")
file.write("Hello World\nWelcome to Python File Handling")
file.close()

file = open("sample.txt", "r")
print(file.read())
file.close()
