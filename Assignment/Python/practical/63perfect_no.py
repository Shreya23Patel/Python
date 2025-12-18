def is_perfect(num):
    total = 0

    for i in range(1, num):
        if num % i == 0:
            total = total + i

    if total == num:
        print(num, "is a Perfect Number")
    else:
        print(num, "is NOT a Perfect Number")



n = int(input("Enter a number: "))
is_perfect(n)
