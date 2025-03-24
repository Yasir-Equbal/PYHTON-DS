import numpy as np


def triangle_check(a, b, c):
    # Check if sides form a valid triangle
    return a + b > c and b + c > a and a + c > b

def heron_area(a, b, c):
    if not triangle_check(a, b, c):
        return "Invalid triangle"
    s = (a + b + c) / 2
    return np.sqrt(s * (s - a) * (s - b) * (s - c))

# 1. Array containing '1' using ones()
ones_array = np.ones((5, 3, 3), dtype=int)
print("Ones Array:\n", ones_array)

# 2. Zeros array with specific shape and data type
zeros_array = np.zeros((4, 2, 3), dtype=int)
print("Zeros Array (int):\n", zeros_array)

# 3. Zeros array without dtype (defaults to float)
zeros_float = np.zeros((4, 2, 3))
print("Zeros Array (float):\n", zeros_float)

# 4. Verify dtype of zeros_float
print("Dtype of zeros_float:", zeros_float.dtype)

# 5. Verify dtype of ones_array
print("Dtype of ones_array:", ones_array.dtype)

# 6. Find dimensions using ndim
print("Dimensions of ones_array:", ones_array.ndim)
print("Dimensions of zeros_array:", zeros_array.ndim)
print("Dimensions of zeros_float:", zeros_float.ndim)

# 7. Find shape using shape attribute
print("Shape of ones_array:", ones_array.shape)
print("Shape of zeros_array:", zeros_array.shape)
print("Shape of zeros_float:", zeros_float.shape)

# 8. Create array from 5 to 20 using arange()
arange_array = np.arange(5, 21)
print("Array with arange:", arange_array)

# 9. Array from 1 to 24 with a step of 4
step_array = np.arange(1, 25, 4)
print("Step Array:", step_array)

# 10. Array with 4 equally spaced numbers from 1 to 25
linspace_array = np.linspace(1, 25, 4)
print("Linspace Array:", linspace_array)

# 11. Reshape zeros array to 6 rows and 4 columns
reshaped_zeros = zeros_array.reshape(6, 4)
print("Reshaped Zeros Array:\n", reshaped_zeros)

# 12. Reshape ones array to a 1D array
reshaped_ones = ones_array.reshape(-1)
print("Reshaped Ones Array:", reshaped_ones)

# 13. One-dimensional random array (15 random integers)
random_1d = np.random.randint(50, 100, 15)
print("Random 1D Array:", random_1d)

# 14. Two-dimensional random array (3x5)
random_2d = np.random.randint(50, 100, (3, 5))
print("Random 2D Array:\n", random_2d)

# 15. Three-dimensional random array (2x4x5)
random_3d = np.random.randint(50, 100, (2, 4, 5))
print("Random 3D Array:\n", random_3d)

# 16. Convert a Python list to NumPy array
py_list = list(range(1, 16))
numpy_array = np.array(py_list)
print("Converted NumPy Array:", numpy_array)

# 17. Convert NumPy array back to Python list
converted_list = list(numpy_array)
print("Converted Python List:", converted_list)

# 18. Triangle Validity Check Example
print("Triangle Check (3, 4, 5):", triangle_check(3, 4, 5))
print("Triangle Check (1, 2, 8):", triangle_check(1, 2, 8))

# 19. Heron’s formula calculation
print("Area of Triangle (3, 4, 5):", heron_area(3, 4, 5))

