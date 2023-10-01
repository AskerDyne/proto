# Input for heights in centimeters, separated by spaces
height_input = input("Input a list of student heights (cm): ")
student_heights = height_input.split()

# Convert the height values from strings to integers
for n in range(len(student_heights)):
    student_heights[n] = int(student_heights[n])

# Print the list of student heights after conversion.
print("\nStudent heights (cm):", student_heights)

# Configuration
total_height = 0
num_students = 0

# Math and returns
for height in student_heights:
    total_height += height
print("Total height (cm):", total_height)

for student in student_heights:
    num_students += 1
print("Number of students:", num_students)

average_height = round(total_height / num_students)
print("Average height (cm):", average_height,"\n")
