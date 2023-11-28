# Create two sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Get the union of the two sets
union = set1.union(set2)
print("Union:", union)

# Get the intersection of the two sets
intersection = set1.intersection(set2)
print("Intersection:", intersection)

# Update set1 with elements in set2
set1.update(set2)
print("Updated set1:", set1)

# Get the symmetrical difference between set1 and set2
sym_diff = set1.symmetric_difference(set2)
print("Symmetric Difference:", sym_diff)

# Create another set3 and clear set3
set3 = {9, 10, 11}
set3.clear()
print("Set3 after clearing:", set3)