#Write a NumPy program to create a 3x3 identity matrix and stack it vertically and horizontally.
import numpy as np

identity_matrix = np.identity(3)
vertical_stack = np.vstack((identity_matrix, identity_matrix))
horizontal_stack = np.hstack((identity_matrix, identity_matrix))

print("3x3 Identity Matrix:")
print(identity_matrix)

print("\nVertically Stacked Identity Matrix:")
print(vertical_stack)

print("\nHorizontally Stacked Identity Matrix:")
print(horizontal_stack)