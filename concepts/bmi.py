# Gets weight and height for calculating BMI
height = input("What is your height? (meters): ")
weight = input("What is your weight? (kg): ")

bmi = float(weight) / float(height) ** 2
bmi_as_int = int(bmi)

# Returns based on UK NHS guidelines
print ("\nBMI is equal to:", bmi_as_int)
if bmi_as_int <= 18.5:
    print("You are: underweight.\n")
elif bmi_as_int <= 25:
    print("You are: a normal weight.\n")
elif bmi_as_int <= 30:
    print("You are: overweight.\n")
elif bmi_as_int <= 35:
    print("You are: obese.\n")
elif bmi_as_int >= 35:
    print("You are: clinically obese.\n")