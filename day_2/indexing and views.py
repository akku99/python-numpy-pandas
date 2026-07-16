"""
Day 2: Indexing, Slicing & Views vs Copies
"""
import numpy as np

a = np.arange(24).reshape(4,6)
print("Original:\n", a)

# 1. Bassic Slicing
print("Row 1:", a[1])
print("Column 2:", a[:, 2])
print("Sub-block:\n", a[1:3, 2:5])
print("Reversed rows:\n", a[::-1])

# 2. Slices are VIEWS, not copies
view = a[0:2, 0:2]
view[0,0] = -999
print("Mutating a slice mutates the original array:\n", a)
print("shares memory(a, view):", np.shares_memory(a, view))
print("view.base is a:", view.base is a)

# 3. Fancy indexing ALWAYS returns a COPY, never a view
fancy = a[[0,1], :]
fancy[0,0] = 12345
print("Fancy index copy does NOT affect original:\n", a)
print("shares memory(a,fancy):", np.shares_memory(a, fancy))

# 4. Boolean indexing also returns a COPY
mask = a % 2 == 0
evens = a[mask]
print("Even values (flat, copy):", evens)

# 5. Explicit copy when you need one
safe_copy = a[0:2, 0:2].copy()
safe_copy[:] = 0
print("Explicit .copy() protects original:\n", a)
