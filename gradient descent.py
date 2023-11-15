def f(x, y):
    return x**2 + y**2  # The function we want to minimize - in this case, the minimum surface

def gradient_descent(f, x, y):
    learning_rate = 0.1  # Learning rate - how much we move in each iteration based on the slope
    epsilon = 1e-1  # The threshold value for slope magnitude where we consider reaching max or min
    max_iterations = 1000  # Maximum number of iterations to run the algorithm

    iteration = 0

    while abs(f(x, y)) > epsilon and iteration < max_iterations:
        gradient_x = (f(x + epsilon, y) - f(x, y)) / epsilon  # The slope in the x direction
        gradient_y = (f(x, y + epsilon) - f(x, y)) / epsilon  # The slope in the y direction
        x = x - learning_rate * gradient_x  # Update the value of x based on the slope in the x direction
        y = y - learning_rate * gradient_y  # Update the value of y based on the slope in the y direction
        iteration += 1
        print(f"Iteration {iteration}: x={x}, y={y}")  # Print the x and y values in each iteration

    return x, y

# Initial point
start_x = 10
start_y = 3
result_x, result_y = gradient_descent(f, start_x, start_y)

print(f" x_max: {result_x}, y_max: {result_y}")  # Print the optimal point found
