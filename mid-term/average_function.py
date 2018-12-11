# average_function.py
# For this exercise the pseudo-code is required (in this same file)
# Write a function that calculates the average of the values of
# any vector of 10 numbers
# Each single value of the vector should be read from the keyboard
# and added to a list.
# Print the input vector and its average
# Define separate functions for the input and for calculating the average

''' First, create a function for the input. Since the vector will have 10 numbers the program should ask for
10 keyboard inputs and collects them into a list. In Python 3 inputs are strings so we need to convert this
to numbers.
Then, create a function that computes the average. First, sum all the numbers on the vector and then divide
by the number of elements.
'''

# Input function:
def input_vector():
    vector = []
    print("Give me 10 numbers and I will find the average:")
    for i in range(10):
        # "float(input())" converts the strings to float numbers
        vector.append(float(input()))
    return vector

def average(vector):
    sum_elements = sum(vector)
    total_elements = len(vector)
    average = sum_elements / total_elements
    return average

final_vector = input_vector()
final_average = average(final_vector)
print("This is your vector:", final_vector, "and its average is", final_average)




