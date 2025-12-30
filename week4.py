from collections import namedtuple
from functools import wraps
import time

def execution_logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[LOG] Calling {func.__name__} with args={args} kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"[LOG] {func.__name__} completed\n")
        return result
    return wrapper

def conditional_logger(enabled=True):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if enabled:
                print(f"[LOG-ENABLED] Calling {func.__name__}")
            return func(*args, **kwargs)
        return wrapper
    return decorator

def timed(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        value = func(*args, **kwargs)
        end = time.time()
        print(f"[TIME] {func.__name__} took {end-start:.5f}s")
        return value
    return wrapper

class User:
    active_users = 0

    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        User.active_users += 1

    def role_description(self):
        return "Generic system user"

    def __del__(self):
        User.active_users -= 1

    @classmethod
    def from_serialized(cls, serialized_str):
        user_id, name = serialized_str.split("|")
        return cls(user_id, name)

    @staticmethod
    def validate_name(name):
        return name.isalpha()

    def __str__(self):
        return f"User({self.user_id}, {self.name})"

    def __repr__(self):
        return f"User(id={self.user_id!r}, name={self.name!r})"

    def __len__(self):
        return len(self.name)

    def __eq__(self, other):
        return self.user_id == other.user_id

    def __lt__(self, other):
        return self.name < other.name

    def __call__(self):
        return f"{self.name} invoked like function!"

class Admin(User):
    def role_description(self):
        return "Administrator — full access"

class Guest(User):
    def role_description(self):
        return "Guest user — read only"

class Editor(User):
    def role_description(self):
        return "Editor — content management"

class DataStreamer:
    def __init__(self, data):
        self.data = data

    def lazy_stream(self):
        for item in self.data:
            yield item

Config = namedtuple("Config", "system_name version")

class SystemConfigStore:
    def __init__(self):
        self._configs = {}

    def add_config(self, key, config):
        self._configs[key] = config

    def get_config(self, key):
        return self._configs.get(key)

def find_user_by_name(users, target):
    for user in users:
        if user.name == target:
            print("User found:", user)
            break
    else:
        print("User not found (for/else executed)")

@execution_logger
@timed
def run_system_demo():
    print("\n--- User creation & lifecycle demo ---")
    u1 = Admin("101", "Sanjeev")
    u2 = Guest("102", "Riya")
    u3 = Editor.from_serialized("103|Arjun")
    print(u1.role_description())
    print(u2.role_description())
    print(u3.role_description())
    print("\nActive users =", User.active_users)
    print("Name valid?", User.validate_name("Sanjeev123"))
    print(str(u1))
    print(repr(u2))
    print("Length of name =", len(u3))
    print("Equality check =", u1 == u2)
    print("Call object =", u1())
    print("\n--- Lazy Data Streaming ---")
    ds = DataStreamer(range(5))
    gen = ds.lazy_stream()
    print(next(gen))
    print(next(gen))
    print(list(gen))
    print("\n--- Immutable Config ---")
    store = SystemConfigStore()
    c = Config("UserSystem", "1.0")
    store.add_config("main", c)
    print(store.get_config("main"))
    print("\n--- Loop ELSE demo ---")
    find_user_by_name([u1, u2, u3], "XYZ")
    print("\n--- Comparison sorting demo ---")
    print(sorted([u1, u2, u3]))

if __name__ == "__main__":
    run_system_demo()
