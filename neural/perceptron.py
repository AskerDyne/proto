x_input = [0.1, 0.5, 0.2] # Inputs
w_weights = [0.4, 0.3, 0.6] # Weights
threshold = 0.5 # Threshold

# Define a step to determine output of the perceptron
def step(weighted_sum):
    if weighted_sum > threshold:
        return 1 # If weight exceeds threshold, return 1 (class 1)
    else:
        return 0 # Otherwise, return 0 (class 0)

# Performs a simple classification task based on the inputs, weights, and threshold, this demonstrates the basic concept of a perceptron
def perceptron():
    weighted_sum = 0

    # Calculate the weighted sum by multiplying each input by its corresponding weight
    for x, w in zip(x_input, w_weights):
        weighted_sum += x * w
        print(weighted_sum)

    # Uses step function to determine output (classification)
    return step(weighted_sum)

output = perceptron()
print("output: " + str(output))