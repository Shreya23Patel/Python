with open("sample.txt", "r") as source_file:
    content = source_file.read()  # Read all content

with open("read.txt", "w") as dest_file:
    dest_file.write(content)      # Write to destination

print("File copied successfully!")
