# a. 
set1 = set()

# b.
set1.update(["eu", "sihyeon", "mia", "onda", "aisha", "yiren"])

# c.
set2 = {"flower", "eu", "ace", "cute","vampire", "yiren"}

# d.
print(f"Union: {set1 | set2}\nDifference(set1 - set2): {set1 - set2}\nDifference(set2 - set1): {set2 - set1}\nSymmetric difference: {set1 ^ set2}\nIntersection: {set1 & set2}")

# e.
set1 -= set1 & set2
set2 -= set1 & set2

# f.
set1.clear()
set2.clear()
