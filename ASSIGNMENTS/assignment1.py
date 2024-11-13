# Perimeter and Area of Rectangle
length = int(input("Enter length of the rectangle: "))
breadth = int(input("Enter breadth of the rectangle: "))
print("Perimeter of the rectangle: ", 2*(length+breadth), "units")
print("Area of the rectangle: ", length*breadth, "sq. units")

# Area and Circumference of a circle
import math
radius = int(input("Enter the radius of the circle: "))
print("Area of the circle = ", math.pi * (radius ** 2), "sq. units")
print("Circumference of the circle = ", 2 * math.pi * radius, "units")

# Simple Interest
principal = int(input("Enter principal amount: Rs."))
rate = float(input("Enter rate of interest: "))
time = int(input("Enter the time in years: "))
print("Simple Interest = Rs.",(principal*rate*time)/100)

# Temperature Conversion
celsius = float(input("Enter the temperature in celsius: "))
print("Farenheit = ", ((9*celsius)/5)+32)

# Even Odd
num = int(input("Enter a number: "))
if (num%2==0):
    print(num," is even.")
else:
    print(num," is odd.")

# name = input("Enter name: ")
# colour = input("Enter your favorite color: ")
# message = f"Hello {name}! Your favorite color is {colour}."
# print(message)

# string = input("Enter a string: ")
# print("Reverse of the string = ",string[::-1])

# string = input("Enter a string: ")
# char = input('Enter the character to search: ')
# print(f"The character {char} appears",string.count(char),"times.")

# Palindrome
string = input("Enter a string: ")
if string==string[::-1]:
    print("The string is a palindrome.")
else:
    print("Not a palindrome.")

# Comparison of Integers
num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
if num1>num2:
    print(f"{num1} is greater than {num2}.")
elif num1<num2:
    print(f"{num1} is lesser than {num2}.")
else:
    print(f"{num1} is equal to {num2}.")

# Grade Checker
marks = int(input("Enter the marks secured: "))
if marks>=90 and marks<=100:
    print("Grade: A")
elif marks>=80 and marks<=89:
    print("Grade: B")
elif marks>=70 and marks<=79:
    print("Grade: C")
elif marks>=60 and marks<=69:
    print("Grade: D")
else:
    print("Grade: F")

# year = int(input("Enter a year: "))
# if (year%100!=0 and year%4==0) or (year%400==0):
#     print("It is a leap year.")
# else:
#     print("It is not a leap year.")

# Fibonacci Series
f0 = 0
f1 = 1
n = int(input("Enter the end of series: "))
print(f0, f1, end = " ")
for i in range(2,n):
    temp = f0+f1
    print(temp, end=" ")
    f0=f1
    f1=temp

