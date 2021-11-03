"""
Date: August 9th, 2021

Purpose: This file contains the basics of Arrays in python
and the common operations performed using this Data Structures.
"""

# Import from 'array' module
import array

# Initializing array
arr = array.array('i', [1, 2, 3, 7, 4, 2, 1, 5, 7, 8, 9, 4, 3, 6, 5])

print("The new array created is: ", end=" ")

for i in range(0, len(arr)):
    print(arr[i], end=" ")


# APPEND: Using 'append()' to insert a new value at the end.
arr.append(4)

# Print new values
print("The values after append are: ", end=" ")
for i in range(0, len(arr)):
    print(arr[i], end=" ")

# INSERT: in specific position
arr.insert(2, 5)

print("\r")

# Print new values
print("The array values after Inserting are: ", end=" ")
for i in range(0, len(arr)):
    print(arr[i], end=" ")

print("\r")

# Using POP to remove an element from 2nd position
print(arr.pop(2))

# Print elements
print("The array elements after popping: ", end=" ")
for i in range(0, len(arr)):
    print(arr[i], end=" ")

print("\r")

# REMOVE to remove the first occurence of an element
arr.remove(1)

# Print all the elements
print("The array elements after removing first occurence of 1 are: ", end=" ")
for i in range(0, len(arr)):
    print(arr[i], end=" ")

print("\r")

# INDEX to get the index of first occurence of an element
print("The first occurence of 3 in the array is: {}".format(arr.index(3)), end=" ")

print("\r")

# REVERSE the array values
arr.reverse()

# Print all the values after reverse
print("The array elements after reversing are: ", end=" ")
for i in range(0, len(arr)):
    print(arr[i], end=" ")
