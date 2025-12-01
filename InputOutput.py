name=input("Enter Your Name")
print("Welcome",name,"to the Python Team")
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
print(f"Sum={a+b} Sub={a-b} Multiply={a*b} Divide={a/b}")
names = input("Enter names separated by commas: ")
name_list = names.split(",")
print("Names List:", name_list)
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")
value = 3.14159
print(f"{value:.2f}")



