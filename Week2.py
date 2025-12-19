from functools import reduce

a = [1, 2, 3, 4]
doubled = list(map(lambda x: x * 2, a))
print(doubled)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)

words = ["apple", "banana", "cherry", "date"]
longest_word = reduce(lambda a, b: a if len(a) > len(b) else b, words)
print(longest_word)

my_floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59]
squared_rounded = list(map(lambda x: round(x ** 2, 1), my_floats))
print(squared_rounded)

my_names = ["olumide", "akinremi", "josiah", "temidayo", "omoseun"]
short_names = list(filter(lambda name: len(name) <= 7, my_names))
print(short_names)

nums = [1, 2, 3, 4, 5]
total_sum = reduce(lambda a, b: a + b, nums)
print(total_sum)

numbers = [1, 2, 3, 4, 5]
all_positive = all(n > 0 for n in numbers)
print(all_positive)

numbers = [1, 3, 5, 7, 8]
any_even = any(n % 2 == 0 for n in numbers)
print(any_even)

numbers = [3, 7, 10, 14, 25]
divisible_by_5 = [n for n in numbers if n % 5 == 0]
print(divisible_by_5)

fruits = ["apple", "banana", "cherry"]

for index, value in enumerate(fruits):
    print(index, value)


person = {"name": "Alice", "age": 30, "city": "New York"}

for key, value in person.items():
    print(f"{key}: {value}")


fruits = ["apple", "banana", "cherry", "date", "elderberry"]

even_index_fruits = [(index, value) for index, value in enumerate(fruits, start=1) if index % 2 == 0]
print(even_index_fruits)

numbers = [1, 32, 63, 14, 5, 26, 79, 8, 59, 10]
print(max(numbers), min(numbers))


setn = {5, 10, 3, 15, 2, 20}
print(max(setn), min(setn))


def shortest_and_longest(words):
    shortest = min(words, key=len)
    longest = max(words, key=len)
    return shortest, longest


words = ["apple", "banana", "kiwi", "grapefruit", "orange"]
print(shortest_and_longest(words))

a = 10
b = 0

try:
    result = a / b
    print(result)
except ZeroDivisionError as e:
    print(e)


my_list = [1, 2, 3]

try:
    print(my_list[5])
except IndexError as e:
    print(e)


def safe_divide(a, b):
    try:
        result = a / b
        print(f"Result: {result}")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed")
    except TypeError:
        print("Error: Invalid data type for division")
    finally:
        print("Execution completed")


safe_divide(1, 0)
safe_divide(1, "a")

import time
from functools import wraps


def time_calculator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print("Start Time:", start_time)
        print("End Time:", end_time)
        print("Total Time Taken:", end_time - start_time)
        return result
    return wrapper


@time_calculator
def append_numbers():
    numbers = []
    for i in range(1, 1001):
        numbers.append(i)
    return numbers


append_numbers()


def retry(times):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, times + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Attempt {attempt} failed:", e)
            print("All retry attempts failed")
        return wrapper
    return decorator


@retry(3)
def may_fail(name):
    print(f"Hello, {name}!")


may_fail("Sanjeev")


def validate_positive(func):
    @wraps(func)
    def wrapper(x):
        if x <= 0:
            raise ValueError("Input must be a positive number")
        return func(x)
    return wrapper


@validate_positive
def square_root(x):
    return x ** 0.5


print(square_root(9))


def cache(func):
    cached_results = {}

    @wraps(func)
    def wrapper(*args):
        if args in cached_results:
            return cached_results[args]
        result = func(*args)
        cached_results[args] = result
        return result
    return wrapper


@cache
def expensive_computation(x):
    print("Performing computation...")
    return x * x


print(expensive_computation(5))
print(expensive_computation(5))


def requires_permission(func):
    @wraps(func)
    def wrapper(user, *args, **kwargs):
        if "admin" in user.get("permissions", []):
            return func(user, *args, **kwargs)
        else:
            print("Access denied")
    return wrapper


@requires_permission
def delete_user(user, user_id):
    print(f"User {user_id} deleted by {user['name']}")


user1 = {'name': 'Alice', 'permissions': ['admin']}
user2 = {'name': 'John', 'permissions': ['dev']}
user3 = {'name': 'Kurt', 'permissions': ['test']}

delete_user(user1, 101)
delete_user(user2, 102)
delete_user(user3, 103)

def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


fib = fibonacci()
for _ in range(10):
    print(next(fib))


def infinite_multiples(n):
    multiple = n
    while True:
        yield multiple
        multiple += n


multiples = infinite_multiples(3)
for _ in range(5):
    print(next(multiples))


def repeat_word(word, times):
    for _ in range(times):
        yield word


for value in repeat_word("hello", 5):
    print(value)

import csv


with open("sample.txt", "r") as file:
    content = file.read()
    print(content)


with open("words.txt", "r") as file:
    word_count = len(file.read().split())
    print(word_count)


with open("output.txt", "w") as file:
    file.write("Hello, Python!")


data = [
    ["Name", "Roll Number", "Marks"],
    ["Alice", "101", "85"],
    ["Bob", "102", "90"],
    ["Charlie", "103", "88"]
]

with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)


def read_large_file(filename):
    with open(filename, "r") as file:
        for line in file:
            yield line.strip()


for line in read_large_file("sample.txt"):
    print(line)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


person = Person("Alice", 25)
print(person.name)
print(person.age)


class BankAccount:
    def __init__(self, account_number, customer_name, balance=0):
        self.account_number = account_number
        self.customer_name = customer_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient balance")

    def check_balance(self):
        return self.balance


account = BankAccount("12345", "Bob", 1000)
account.deposit(500)
account.withdraw(300)
print(account.check_balance())


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    @classmethod
    def from_string(cls, data):
        title, author = data.split(", ")
        return cls(title, author)


book = Book.from_string("Python Programming, John Doe")
print(book.title)
print(book.author)


class Animal:
    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):
    def sound(self):
        print("Dog barks")


class Cat(Animal):
    def sound(self):
        print("Cat meows")


dog = Dog()
cat = Cat()
dog.sound()
cat.sound()


class Father:
    def skills(self):
        print("Gardening")


class Mother:
    def skills(self):
        print("Cooking")


class Child(Father, Mother):
    def skills(self):
        Father.skills(self)
        Mother.skills(self)
        print("Programming")


child = Child()
child.skills()

from datetime import datetime, timedelta
import os


original_date = datetime(2020, 3, 22, 10, 0)
new_date = original_date + timedelta(weeks=1, hours=12)
print(original_date)
print(new_date)


today = datetime.today().date()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)
print(yesterday)
print(today)
print(tomorrow)


cwd = os.getcwd()
print(cwd)

os.mkdir("test")
print(os.listdir(cwd))

os.rmdir("test")


with open("old_name.txt", "w") as file:
    file.write("sample")

os.rename("old_name.txt", "new_name.txt")


with open("example.txt", "w") as file:
    file.write("Hello File")

file_size = os.path.getsize("example.txt")
print(file_size)


date_string = "Feb 25 2020 4:20PM"
converted_date = datetime.strptime(date_string, "%b %d %Y %I:%M%p")
print(converted_date)


date_to_subtract = datetime(2025, 2, 25)
new_date = date_to_subtract - timedelta(days=7)
print("New date:", new_date.date())


formatted_date = datetime(2020, 2, 25)
print(formatted_date.strftime("%A %d %B %Y"))
