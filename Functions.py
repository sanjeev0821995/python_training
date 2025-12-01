# 1. Function to calculate area of a rectangle with default width = 10
def calculate_area(length, width=10):
    return length * width


# 2. Recursive function to compute factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


# 3. Function to reverse a string and return it
def reverse_string(s):
    rev = ""
    for ch in s:
        rev = ch + rev
    return rev


# 4. Function that sums all numbers from two lists
def sum_two_lists(a, b):
    return sum(a) + sum(b)


# 5. Function to return a distinct + sorted list
def distinct_sorted_list(lst):
    return sorted(set(lst))


# ------------------ TESTING THE FUNCTIONS ------------------

# 1. calculate_area
print("Area:", calculate_area(5))
print("Area:", calculate_area(5, 4))

# 2. factorial
print("Factorial of 5:", factorial(5))

# 3. reverse_string
print("Reverse of 'hello':", reverse_string("hello"))

# 4. sum_two_lists
a = [8, 2, 3, 0, 7]
b = [3, -2, 5, 1]
print("Sum of lists:", sum_two_lists(a, b))

# 5. distinct_sorted_list
lst = [4, 1, 2, 3, 3, 1, 3, 4, 5, 1, 7]
print("Distinct + Sorted:", distinct_sorted_list(lst))
