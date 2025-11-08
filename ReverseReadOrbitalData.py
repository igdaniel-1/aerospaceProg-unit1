# Unit 1 - Question 5 part B

# This program is the reverse program of Question 5A

# The data from Question 5 is read into a new file "orbital_details" in a column format with a header
# This program reads from the "orbital_details" file
# The header is removed so that the data can be converted from it's stringified rows, back into an array of values
# The Transpose method is used to rotate the data 90 degrees
# This positions each pre-exisiting column as a row
# In row form, the data of each category is read into an array
# These arrays are returned in the format they were initially given in Question 5A

import numpy as np
# data = np.loadtxt("orbital_details.txt")

with open("orbital_details.txt", "r") as document:
    content = document.readlines()

data = content[1:]
cleaned_data = []

for line in data:
    # remove end-of-line breaks
    # split into array values at tabs
    
    line = line.strip("\n")
    line = line.split("\t")
    # store new arrays of data from each row in the new data structure
    cleaned_data.append(line)


rotated_data = np.transpose(cleaned_data)
# print("rotated_data",rotated_data)

# using the structure from Question 5A 
planet_name = rotated_data[0]
orbital_period = rotated_data[1]
axial_tilt = rotated_data[2]


print("Planet Name:", planet_name)
print("Orbital Period:", orbital_period)
print("Axial Tilt:", axial_tilt)