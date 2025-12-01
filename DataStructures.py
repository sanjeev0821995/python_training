# 1. Given a list of numbers, find and print the maximum and minimum values.
nums = [1, 2, 3, 4, 5]
print("Max:", max(nums))
print("Min:", min(nums))

# 2. Merge two lists and print
a = [1, 2, 3, 4]
b = [5, 6, 7, 8]
merged_list = a + b
print("Merged List:", merged_list)

# 3. Count how many times 3 appears in the list
a = [1, 3, 4, 5, 2, 1, 3, 9, 3]
print("Count of 3:", a.count(3))

# 4. Sort the list and print
print("Sorted List:", sorted(a))

# 5. Add element 6 to a set
numbers = {1, 2, 3, 4, 5}
numbers.add(6)
print("After Adding 6:", numbers)

# 6. Remove element 3 from the set
numbers = {1, 2, 3, 4, 5}
numbers.remove(3)
print("After Removing 3:", numbers)

# 7. Intersection of two sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print("Intersection:", set1.intersection(set2))

# 8. Count occurrences of 'apple' in tuple
fruits = ('apple', 'banana', 'apple', 'cherry')
print("Count of 'apple':", fruits.count('apple'))

# 9. Concatenate two tuples
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
print("Concatenated Tuple:", tuple1 + tuple2)

# 10. Print value of key "age" from dictionary
person = {"name": "Alice", "age": 30, "city": "New York"}
print("Age:", person["age"])

# 11. Add new key "gender" with value "M"
person["gender"] = "M"
print("After Adding Gender:", person)

# 12. Remove key "city"
person.pop("city")
print("After Removing City:", person)

# 13. Merge two dictionaries
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
merged_dict = {**dict1, **dict2}
print("Merged Dictionary:", merged_dict)
