# Loop through numbers from 1 to 100 inclusive
for number in range(1, 101):
    output = ""

    # Check if the number is divisible by 3 and 5
    if number % 3 == 0 and number % 5 == 0:
        output = "FizzBuzz"

    # Check if the number is divisible by 3
    if number % 3 == 0:
        output = "Fizz"

    # Check if the number is divisible by 5
    if number % 5 == 0:
        output = "Buzz"

    # If none of the above conditions match, convert the number to a string
    if output == "":
        output = str(number)
    print(output)
