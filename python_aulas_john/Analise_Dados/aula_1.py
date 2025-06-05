import numpy as np

arr1d = np.array([1,2,3])
print(f"Array 1D: {arr1d}, Dimensões: {arr1d.ndim}")

arr2d = np.array([[1,2,3,4,5],[5,6,7,8,9]])
print(f"Array 2D: {arr2d}, Dimensões: {arr2d.ndim}")

arr3d = np.array([
    [[0, 5, 6], [5, 8, 9]],  # Primeira matriz 2x3
    [[4, 5, 6], [5, 9, 8]]    # Segunda matriz 2x3
])
print(f"Array 3D: {arr3d}, Dimensões: {arr3d.ndim}")

# Shape
# Indica o tamanho do array
print(f"Shape arr1d: {arr1d.shape}")
print(f"Shape arr2d: {arr2d.shape}")
print(f"Shape arr3d: {arr3d.shape}")