# Imports
import numpy as np

class SigmoidPerceptron:
    # Initialise Sigmoid Perceptron with the number of input features
    def __init__(self, num_features):
        self.num_features = num_features
        self.weights = np.zeros(num_features) # Set weights to zeros
        self.bias = 0.0 # Set bias to zero

    # Sigmoid activation
    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    # Prediction for a singular input
    def predict(self, x):
        weighted_sum = np.dot(self.weights, x) + self.bias
        return self.sigmoid(weighted_sum)

    # Train the Sigmoid Perceptron with mild training data
    def train(self, X, y, learning_rate=0.1, epochs=100):
        for _ in range(epochs):
            for i in range(len(X)):
                x_i = X[i] # Input features for singular data point
                y_i = y[i] # Target labelling for the data point
                prediction = self.predict(x_i) # Generate a prediction
                error = y_i - prediction # Calculate the prediction error

                # Update based on prior error
                self.weights += learning_rate * error * x_i
                self.bias += learning_rate * error

    # Make predictions for multiple input data points
    def predict_batch(self, X):
        return [self.predict(x) for x in X]

try:
    # Supplied training data
    X_train = np.array([[0.1, 0.2], [0.4, 0.5], [0.7, 0.8]])
    y_train = np.array([0, 1, 1])

    # Create and train sigmoid perceptron
    model = SigmoidPerceptron(num_features=2)
    model.train(X_train, y_train)

    # Sample test data
    X_test = np.array([[0.2, 0.3], [0.6, 0.7]])

    # Return predictions
    predictions = model.predict_batch(X_test)
    print("Predictions:", predictions)

except Exception as e:
    # Handle exceptions gracefully, e.g., by printing an error message
    print("An error occurred:", e)