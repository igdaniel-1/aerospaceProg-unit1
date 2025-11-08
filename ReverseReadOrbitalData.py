# Unit 1 - Question 5 part B

import numpy as np
# data = np.loadtxt("orbital_details.txt")

with open("orbital_details.txt", "r") as document:
    content = document.readlines()

data = content[1:]
# print(data)
data = np.transpose(data)
print(data)


# name = data[0]
# orbital_period = data[1]
# axial_tilt = data[2]


# print(name)