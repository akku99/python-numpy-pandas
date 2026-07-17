"""
Day 3: Data Types, Casting & Memory Layout
"""
import numpy as np

# 1. dtype hierarchy and precision

for dt in [np.int8, np.int32, np.int64, np.float16, np.float32, np.float64]:
    info = np.iinfo(dt) if np.issubdtype(dt, np.integer) else np.finfo(dt)
    print(dt.__name__, "->", info)

# 2. Overflow pitfalls with small integer types
small = np. array([127], dtype=np.int8)
print("int8 127 + 1 overflows to:", small + np.int8(1))

# 3. C-order vs Fortran-order memory layout
c_arr = np.array([[1,2,3], [4,5,6]], order = "C")
f_arr = np.array([[1,2,3], [4,5,6]], order = "F")
print("C flags:", c_arr.flags["C_CONTIGUOUS"], c_arr.flags["F_CONTIGUOUS"])
print("F flags:", f_arr.flags["C_CONTIGUOUS"], f_arr.flags["F_CONTIGUOUS"])

# 4. Strides: bytes to step per axis
a = np.arange(12).reshape(3,4)
print("strides of (3,4) int64 array:", a.strides) #(32,8)
t = a.T
print("strides of transposed (4,3) int64 array:", t.strides) #(8,32)

# 5. reshape vs ravel vs flatten (view vs copy semantics)
r = a.reshape(4,3)      # view when possible
rv = a.ravel()          # view when possible
fl = a.flatten()        # always a copy
print("reshape shares memory:", np.shares_memory(a, r))
print("ravel shares memory:", np.shares_memory(a, rv))
print("flatten shares memory:", np.shares_memory(a, fl))