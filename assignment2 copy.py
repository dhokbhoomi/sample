import numpy as np

# Creating a NumPy array
arr = np.array([1, 5, 3, 4, 2])
print("Original NumPy array:", arr)

# Iterating through the array
print("\nIteration through NumPy array:")
for x in arr:
    print(x)

# Searching for the number '2'
index = np.where(arr == 2)
print("\nIndex of element '2' in NumPy array:", index)

# Inserting number '10' after number '2' at index 2
arr1 = np.insert(arr, 2, 10)
print("\nArray after insertion:", arr1)

# Deleting the element at index 2
arr = np.delete(arr, 2)
print("Array after deletion:", arr)

# Comparison with Python lists

# Creating a Python list
lst = [1, 5, 3, 4, 2]
print("\nOriginal Python list:", lst)

# Iterating through the list
print("\nIteration through Python list:")
for x in lst:
    print(x)

# Searching for the number '2'
index = lst.index(2)
print("\nIndex of element '2' in Python list:", index)

# Inserting number '10' after number '2' at index 2
lst.insert(2, 10)
print("\nList after insertion:", lst)

# Deleting the element at index 2
del lst[2]
print("List after deletion:", lst)
