def check_range(num, start, end):
    if num >= start and num <= end:
        print(num, "is in the given range")
    else:
        print(num, "is NOT in the given range")


num = int(input("Enter number to check: "))
start = int(input("Enter range start: "))
end = int(input("Enter range end: "))

check_range(num, start, end)
