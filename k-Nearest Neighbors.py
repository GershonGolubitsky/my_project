import numpy as np
from sklearn import datasets

# Load the Iris dataset
iris = datasets.load_iris()

# Creating indices for the dataset and shuffling them
indices = np.arange(len(iris.data))
np.random.shuffle(indices)

# Separating the data into two parts: 80% training data and 20% testing data
data = int(0.8 * len(indices))
first_part_indices = indices[:data]
second_part_indices = indices[data:]

# Dividing the dataset based on the indices
first_part_data = iris.data[first_part_indices]
second_part_data = iris.data[second_part_indices]

# Extracting target values for the first and second parts
first_part_target = iris.target[first_part_indices]
second_part_target = iris.target[second_part_indices]

# List to store selected targets for each point in the second part
selected_targets = []

# Loop through each point in the second part to find the selected target
for point in second_part_data:
    # Calculate distances between the point in the second part and the first part
    distances = np.sqrt(np.sum((first_part_data - point) ** 2, axis=1))

    # Finding the indices of the n closest points in the first part to the current point in the second part
    closest_indices = np.argsort(distances)[:10]

    # Count the occurrences of each target value in the closest points
    count_zeros = np.count_nonzero(first_part_target[closest_indices] == 0)
    count_ones = np.count_nonzero(first_part_target[closest_indices] == 1)
    count_twos = np.count_nonzero(first_part_target[closest_indices] == 2)

    # Determining the selected target based on the majority in the closest points
    if count_zeros > count_ones and count_zeros > count_twos:
        selected_target = 0
    elif count_ones > count_zeros and count_ones > count_twos:
        selected_target = 1
    else:
        selected_target = 2

    selected_targets.append(selected_target)

# Check how many targets in the second part match the selected targets
match_count = np.count_nonzero(second_part_target == selected_targets)

# Displaying the results
print("Number of rows in the test data:", len(second_part_data))
print("Number of matches between second_part_target and selected_target:", match_count)

# print("Test data:",second_part_data)
# print("Selected Targets for each point in second data:", selected_targets)

# import numpy as np
# from sklearn import datasets
#
# iris = datasets.load_iris()
#
# indices = np.arange(len(iris.data))  # Create a list of original indices
# np.random.shuffle(indices)  # Shuffle the indices
#
# data = int(0.8 * len(indices))  # Size of the first part, 80% of the total indices
# first_part_indices = indices[:data]  # Indices of the first part
#
# second_part_indices = indices[data:]  # Indices of the second part
#
# first_part_data = iris.data[first_part_indices]  # Data of the first part
# second_part_data = iris.data[second_part_indices]  # Data of the second part
#
# first_part_target = iris.target[first_part_indices]  # Targets of the first part
# second_part_target = iris.target[second_part_indices]  # Targets of the second part
#
# random_index = np.random.choice(second_part_indices) # Random row
#
# first_part_data = iris.data[first_part_indices]
# random_point = iris.data[random_index]
#
# distances = np.sqrt(np.sum((first_part_data - random_point) ** 2, axis=1))
# closest_indices = np.argsort(distances)[:10]
#
# count_zeros = np.count_nonzero(first_part_target[closest_indices] == 0)
# count_ones = np.count_nonzero(first_part_target[closest_indices] == 1)
# count_twos = np.count_nonzero(first_part_target[closest_indices] == 2)
#
# if count_zeros > count_ones and count_zeros> count_twos:
#     selected_target = 0
# elif count_ones> count_zeros and count_ones> count_twos:
#     selected_target = 1
# else:
#     selected_target = 2
#
# # if selected_target == random_index:
# #     print( "True")
#
# print("Selected Target:", selected_target)
#
#
# print("Random Index from second part:", random_index)
#
# print("Data at random index:", iris.data[random_index])
#
# print("Distances to the random point using Pythagorean theorem:")
# print(distances)
#
# print(first_part_data, first_part_target)
#

def split_train_test(x,y):
    # return x_train, x_test, y_train, y_test
    pass

def knn_predict(x_train, y_train, x_test):
    pass

def accuracy(y_test, y_pred):
    pass