# -------------------- FOR LOOP --------------------

# 1. Check even or odd
num = int(input("Enter a number: "))
if num % 2 == 0:
    print(num, "is Even")
else:
    print(num, "is Odd")

# 2. Reverse a string using for loop and check palindrome
s = input("Enter a string: ")
reverse_s = ""

for ch in s:
    reverse_s = ch + reverse_s

print("Reversed:", reverse_s)

if s == reverse_s:
    print("Palindrome")
else:
    print("Not Palindrome")

# 3. Fibonacci using user input
n = int(input("Enter N for Fibonacci: "))
a, b = 0, 1

print("Fibonacci Sequence:", end=" ")
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b
print()

# 4. Find two values whose sum is 9
lst = [1, 2, 3, 4, 5]
result = []

for i in range(len(lst)):
    for j in range(i + 1, len(lst)):
        if lst[i] + lst[j] == 9:
            result = [lst[i], lst[j]]
            break
    if result:
        break

print("Two numbers with sum 9:", result)

# -------------------- WHILE LOOP --------------------

# 5. Print even numbers 1 to 20
i = 1
print("Even numbers from 1 to 20:")
while i <= 20:
    if i % 2 == 0:
        print(i, end=" ")
    i += 1
print()

# -------------------- BREAK --------------------

numbers = [10, 20, 30, 40, 50]
search_for = 30

for n in numbers:
    if n == search_for:
        print("Found:", n)
        break

# -------------------- CONTINUE --------------------

print("Odd numbers from 1 to 10:")
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i, end=" ")
print()

# -------------------- PASS --------------------

print("Output of pass example:")
for i in range(5):
    if i == 3:
        pass
    print(i)

# -------------------- MATCH --------------------

day = input("Enter day name: ").lower()

match day:
    case "monday" | "tuesday" | "wednesday" | "thursday" | "friday":
        print("Weekday")
    case "saturday" | "sunday":
        print("Weekend")
    case _:
        print("Invalid day")
