def insert_middle(s, add):
    mid = int(len(s) / 2)
    first_part = s[:mid]
    second_part = s[mid:]
    return first_part + add + second_part


print(insert_middle("Python", "123"))