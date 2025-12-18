n = int(input("Enter number of lines: "))

with open("read.txt", "r") as file:
    lines = file.readlines()

for line in lines[-n:]:
    print(line, end="")
