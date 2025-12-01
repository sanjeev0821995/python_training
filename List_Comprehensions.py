# 1. Convert list of numeric strings to integers
strings = ["1", "2", "3", "4", "5"]
int_list = [int(x) for x in strings]
print("Converted to integers:", int_list)

# 2. Extract integers greater than 10
numbers = [1, 5, 13, 4, 16, 7]
greater_than_10 = [n for n in numbers if n > 10]
print("Greater than 10:", greater_than_10)

# 3. Create list of squares from 1 to 5
squares = [x * x for x in range(1, 6)]
print("Squares:", squares)

# 4. Convert 2D list to 1D list
matrix = [[1, 3, 4], [23, 32, 56, 74], [-2, -6, -9]]
flattened = [x for row in matrix for x in row]
print("Flattened list:", flattened)

# 5. Create dictionary using keys and values lists
keys = ['a', 'b', 'c']
values = [1, 2, 3]
my_dict = {k: v for k, v in zip(keys, values)}
print("Dictionary:", my_dict)

# 6. Dictionary of students scoring above 80
scores = {'Alice': 85, 'Bob': 70, 'Charlie': 90}
high_scores = {name: score for name, score in scores.items() if score > 80}
print("Scores above 80:", high_scores)
