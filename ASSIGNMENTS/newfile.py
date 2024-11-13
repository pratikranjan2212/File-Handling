# a = 5
# b = 8
# print(a*b)
# a = "Hello"
# print(a)

# val = int(input("Enter your value: "))
# print(val)
# print("Type of val: ", type(val))

# printing length
name = input("What is your name? ")
print(name)
print(len(name))

# String Interpolation
name = "Peter"
age = 16
message = f"Hello {name}! You are {age} years old."
print(message)

# Check Integer
num = int(input("Enter a number: "))
if num>0:
    print(f"The number {num} is positive.")
elif num == 0:
    print(f"The number {num} is zero.")
else:
    print(f"The number {num} is negative.")

# Simple if-else statement
age = 18
if age >= 18:
    print("Access Granted.")
else:
    print("Access Denied.")

# Simple Calculator
num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
print("1. Add\n2. Subtract\n3. Multiply\n4. Divide")
op = int(input("Enter operation no: "))
if op==1:
    print(f"The sum of {num1} and {num2} is ",num1+num2)
elif op==2:
    print(f"The difference of {num1} and {num2} is ",num1-num2)
elif op==3:
    print(f"The product of {num1} and {num2} is ",num1*num2)
elif op==4:
    print(f"The quotient of {num1} and {num2} is ",num1/num2)
else:
    print("Invalid choice.")

