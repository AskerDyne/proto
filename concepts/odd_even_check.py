# Gets number, then checks if it can be halved or not
number = int(input("Which number do you want to check?: "))

if number % 2 == 0:
    print(f"\n{number} is even.")
else:
    print(f"\n{number} must be odd!")