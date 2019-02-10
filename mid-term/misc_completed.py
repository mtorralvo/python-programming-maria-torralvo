# miscellaneous.py

#Completed version after the midterm.

# María Torralvo Márquez

# For the following exercises, pseudo-code is not required

# Exercise 1
print("This is Exercise 1:")

# Create a list L of numbers from 21 to 39
# print the numbers of the list that are even
# print the numbers of the list that are multiples of 3

# First, L list is created:
L = []
for i in range(21,40):
    L.append(i)

# Print numbers thar are even:
even_list = []
for i in range(len(L)):
    element = L[i]
    if element%2 == 0:
        even_list.append(element)

print("These are the even numbers of 'L':", even_list)

# Print the multiple of 3:
multiple_list = []
for i in range(len(L)):
    element = L[i]
    if element%3 == 0:
        multiple_list.append(element)

print("These are the multiples of 3 of 'L':", multiple_list)

# Exercise 2
print("This is Exercise 2:")

# Print the last two elements of L
print("These are the last two elements of 'L':", L[-2:])

# Exercise 3
print("This is Exercise 3:")

# What's wrong with the following piece of code? Fix it and
# modify the code in order to have it work AND to have "<i> is in the list"
# printed at least once

# Mistakes on the code:
# ":" missing after "range(10)"
# Quotation marks missing to indicate that the argument of both "print" functions are strings
# Indentation errors
# We need to change the elements of the list from strings to integers to have "<i> is in the list" printed at least once

L = [1, 2, 3]
for i in range(10):
    if i in L:
        print(i, "is in the list")
    else:
        print(i, "not found")

# Exercise 4
print("This is Exercise 4:")

# Read the first line from the sprot_prot.fasta file
# Split the line using 'OS=' as delimiter and print the second element
# of the resulting list
f = open("sprot_prot.fasta")
first_line = f.readline()
split_list = first_line.split('OS=')
print(split_list[1])
f.close()

# Exercise 5
print("This is Exercise 5:")

# Split the second element of the list of Exercise 4 using blanks
# as separators, concatenate the first and the second elements and print
# the resulting string
print(split_list[1].split()[0]+split_list[1].split()[1])

# Exercise 6
print("This is Exercise 6:")

# reverse the string 'asor rosa'
print('asor rosa'[::-1])

# Exercise 7
print("This is Exercise 7:")

# Sort the following list: L = [1, 7, 3, 9]
L = [1, 7, 3, 9]
L.sort()
print(L)

# Exercise 8
print("This is Exercise 8:")

# Create a new sorted list from L = [1, 7, 3, 9] without modifying L
L = [1, 7, 3, 9]
sorted_L = L
sorted_L.sort()
print("This is L:", L)
print("This is the new sorted list:", sorted_L)

# Exercise 9
# Write to a file the following 2 x 2 table:
# 2 4
# 3 6

import numpy as np
table = np.matrix([[2, 4], [3, 6]])
with open("table.txt", "w+") as f:
	for line in table:
		np.savetxt(f, line, fmt='%i')		
f.close

