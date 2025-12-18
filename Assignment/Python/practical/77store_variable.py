file = open("read.txt", "r")

data = ""
for line in file:
    data = data + line

file.close()

print(data)
