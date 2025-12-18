def unique_list(lst):
    new_list = []

    for item in lst:
        if item not in new_list:
            new_list.append(item)

    return new_list

# Example
my_list = [1, 2, 3, 2, 4, 1, 5]
print(unique_list(my_list))
