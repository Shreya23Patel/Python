# Take sentence from user
text = input("Enter a sentence: ")

# Split sentence into words
words = text.split()

# Find maximum word length
max_len = len(words[0])

for word in words:
    if len(word) > max_len:
        max_len = len(word)

# Print longest word
print("Longest word:")
for word in words:
    if len(word) == max_len:
        print(word)
