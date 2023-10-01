# Calculates a tip percentage based on input values
bill = float(input("What is your total bill? [£]: "))
tip = int(input("How much do you want to tip? [%]: "))
split = int(input("How many is the bill split between?: "))

calculation = tip / 100 * bill + bill / split
format_calculation = "{:.2f}".format(calculation)

print(f"\n£{format_calculation} per-person.")