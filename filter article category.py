"""Importing necessary libraries and modules"""
import numpy as np
from sklearn.datasets import fetch_20newsgroups
from typing import Set
import re
from collections import defaultdict

"""Loading the 20newsgroups dataset"""
categories = ['alt.atheism', 'soc.religion.christian', 'comp.graphics', 'sci.med']
train_data = fetch_20newsgroups(subset='train', categories=categories, shuffle=True, random_state=42)
test_data = fetch_20newsgroups(subset='test', categories=categories, shuffle=True, random_state=42)
print(len(train_data.data), len(test_data.data))  # Printing the size of the train and test datasets
data = np.array(train_data.data)

"""Function to tokenize the data"""
def tokenize(data_train: str) -> Set[str]:
    text = data_train.lower()
    all_words = re.findall("[a-z0-9']+", text)
    return set(all_words)

"""Function to preprocess the training data"""
def design_data(train_data):
    for i in range(len(train_data.data)):
        train_data.data[i] = tokenize(train_data.data[i])
    return np.array(train_data.data)

"""Function to split data based on target values"""
def split(target, new_data):
    return new_data[np.where(target == 0)], new_data[np.where(target == 1)], new_data[np.where(target == 2)], new_data[np.where(target == 3)]

"""Function to count word occurrences in the data"""
def count_word_occurrences(data):
    word_counts = defaultdict(int)
    for text in data:
        for word in text:
            word_counts[word] += 1
    for i in word_counts:
        word_counts[i] = word_counts[i] / len(data)
    return word_counts

"""Function to calculate word probability"""
def calculate_word_probability(test, data_counts):
    prob = 1
    for word in test:
        if word not in data_counts:
            prob *= 0.00001
        else:
            prob *= data_counts[word]
    return prob

"""Function to check the main probability for each category"""
def main_check(test, all_dicts):
    all_probs = []
    for d in all_dicts:
        all_probs.append(calculate_word_probability(test, d))
    return np.argmax(np.array(all_probs))

"""Function to calculate the accuracy of the model"""
def calculate_accuracy(test_target, target):
    correct = np.sum(test_target == target)
    total = len(target)
    accuracy = (correct / total) * 100
    return accuracy

"""Main function to execute the entire pipeline"""
def main():
    new_data = design_data(train_data)

    """Splitting data into different categories based on the target labels"""
    data_0, data_1, data_2, data_3 = split(train_data.target, new_data)
    data_0_counts = count_word_occurrences(data_0)
    data_1_counts = count_word_occurrences(data_1)
    data_2_counts = count_word_occurrences(data_2)
    data_3_counts = count_word_occurrences(data_3)

    """Classifying test articles and storing the results"""
    classification_results = []
    for article in test_data.data:
        article_words = tokenize(article)
        category = main_check(article_words, [data_0_counts, data_1_counts, data_2_counts, data_3_counts])
        classification_results.append(category)

    """Calculating and printing the success rate of the classification"""
    test_target = test_data.target
    success_rate = calculate_accuracy(test_target, classification_results)
    print(f"success rate:{success_rate}%")

if __name__ == "__main__":
    main()
