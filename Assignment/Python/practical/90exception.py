try:
    num = int(input("Enter an odd number: "))

    if num % 2 == 0:
        raise ValueError("Even number entered!")

    print("You entered an odd number:", num)

except ValueError as e:
    print("Error:", e)
