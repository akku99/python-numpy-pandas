"""
Day 4: Reshaping, Stacking & Splitting Arrays
"""
import numpy as np

a = np.arange(12)

# 1. Reshaping with -1 inference
print(a.reshape(3, 4))  # Reshape to 3 rows and 4 columns
print(a.reshape(2, -1, 2).shape) # Reshape to 2 rows, inferred columns, and 2 depth

# 2. Transpose / swapaxes /  moveaxis
b = np.arange(24).reshape(2, 3, 4)
print("Original shape:", b.shape)
print("transpose shape:", b.transpose(2,0,1).shape)  # Transpose axes
print("swapaxes(0, 1) shape:" , b.swapaxes(0, 1).shape)  # Swap axes 0 and 1
print("moveaxis shape:", np.moveaxis(b, 0, -1).shape)  # Move axis 0 to the last position

# 3. Stacking arrays
x = np.array([1,2,3])
y = np.array([4,5,6])
print("vstack:\n", np.vstack([x, y]))  # Vertical stack
print("hstack:\n", np.hstack([x,y]))  # Horizontal stack
print("stack (new axis):\n", np.stack([x,y], axis=1))  # Stack along a new axis
print("concatenate:\n", np.concatenate([x,y]))  # Concatenate arrays

# 4. Splitting arrays
m = np.arange(16).reshape(4, 4)
top, bottom = np.vsplit(m ,2)  # Vertical split into two parts
left, right = np.hsplit(m, 2)  # Horizontal split into two parts
print("top:\n", top, "\nbottom:\n", bottom)

# uneven split
uneven_split = np.array_split(np.arange(10), 3)
print("uneven split sizes:", [len(u) for u in uneven_split])  # Sizes of uneven splits

# 5. adding/removing dimensions
v = np.array([1, 2, 3])
print("expand_dimension:", np.expand_dims(v, axis=0).shape)  # Add a new axis at position 0
print("newaxis:", v[: , np.newaxis].shape)  # Add a new axis using np.newaxis
print("squeeze:", np.zeros((1, 3, 1)).squeeze().shape())  # Remove single-dimensional entries from the shape