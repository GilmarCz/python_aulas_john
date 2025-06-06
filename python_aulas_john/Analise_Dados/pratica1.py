import numpy as np

array1d = np.array([1,2,3,4,5])
array2d = np.array([[1,2,3,],[4,5,6]])
print(f"Array 1D: {array1d},\nDimensões: {array1d.ndim},\nShape array1d: {array1d.shape},\nO Dtype dessa array1d é: {array1d.dtype},\nO Itemsize do array1d é: {array1d.itemsize}")
print(f"Array 2D: {array2d},\nDimensões: {array2d.ndim},\nShape array1d: {array2d.shape},\nO Dtype dessa array2d é: {array2d.dtype},\nO Itemsize do array2d é: {array2d.itemsize}")

print(f"Array 1D: {array1d}")
print(f"Dimensões: {array1d.ndim}")
print(f"Shape array1d: {array1d.shape}")
print(f"O Dtype dessa array1d é: {array1d.dtype}")
print(f"O Itemsize do array1d é: {array1d.itemsize}")

print(f"Array 2D: {array2d}")
print(f"Dimensões: {array2d.ndim}")
print(f"Shape array1d: {array2d.shape}")
print(f"O Dtype dessa array2d é: {array2d.dtype}")
print(f"O Itemsize do array2d é: {array2d.itemsize}")