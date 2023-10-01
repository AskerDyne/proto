# Takes user input of height in centimeters
height = int(input("How tall are you? (cm): "))

# Check if the height is sufficient to ride the rollercoaster (at least 120cm) and price associated
if height >= 120:
    age = int(input("\nYou can ride the rollercoaster, but what is your age? (years): "))
    if age <= 12:
        price = 5
        print(f"\n{age} year olds must pay £5.\n")
    elif age <= 18:
        price = 7.50
        print(f"\n{age} year olds must pay £7.50.\n")
    elif age >= 45 and age <= 55:
        price = 0
        print(f"\n{age} year olds don't have to pay, it's free!")
    else:
        price = 10
        print(f"\n{age} year olds must pay £10.\n")
    # Offers additionals
    photo_req = input("Do you want a photo for an extra £3? (yes/no): ")
    
    # Calculate the final bill based on whether the user wants a photo
    if photo_req == "yes":
        photo_cost = 3
        bill = price + photo_cost
        print(f"\nYour total is £{bill}, enjoy the ride!\n")
    elif photo_req == "no":
        bill = price
        print(f"\nYour final bill is £{bill}, enjoy the ride!\n")
    else:
        print("\nInvalid input for photo request. Please enter 'yes' or 'no'.")
else:
    # If the height is not sufficient, inform the user
    print(f"\nYou must be over 120cm to ride. Your height is {height}cm, which isn't tall enough. Sorry!")