# Takes inputs
name1 = input("\nWhat is your name?: ")
name2 = input("What is their name?: ")

# Configuration
combined_string = name1 + name2
lower_case = combined_string.lower()

t = lower_case.count("t")
r = lower_case.count("r")
u = lower_case.count("u")
e = lower_case.count("e")
true_score = t + r + u + e

l = lower_case.count("l")
o = lower_case.count("o")
v = lower_case.count("v")
e = lower_case.count("e")
love_score = l + o + v + e

# Combine true and love scores
love_score = int(str(true_score) + str(love_score))

# Determine the relationship message based on the love score
if (love_score < 10) or (love_score > 90):
    print(f"Your score is: {love_score}, you go together like mentos and coke!")
elif (love_score >= 40) and (love_score <= 50):
    print(f"It's genuine true love, a beautiful score of {love_score}!")
else:
    print(f"Your score was: {love_score}")