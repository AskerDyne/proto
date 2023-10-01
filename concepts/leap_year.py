# Takes year and does the math to determine if it's a leap year
year = int(input("What year is it? (year): "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("\nYou are in a leap year!\n")
        else:
            print("\nIt is not a leap year.")
    else:
        print("\nIts a leap year!")
else:
    print("\nIt is not a leap year.")