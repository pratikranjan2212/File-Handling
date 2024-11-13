# #1 Power of a Number
# num = int(input("Enter a number: "))
# pow = int(input("Enter its power: "))
# print("The power of", num, "is", num**pow)

# #2 Check input
# num = int(input("Enter a number: "))
# if num==0:
#     print("The input number is zero.")
# else:
#     print("The input number is non-zero.")

# #3 Check number for positive and negative
# num = int(input("Enter a number: "))
# if num>0:
#     print("The input number is positive.")
# elif num==0:
#     print("The input number is zero.")
# else:
#     print("The input number is negative.")

# #4 Compare two numbers
# num1 = int(input("Enter a number: "))
# num2 = int(input("Enter a number: "))
# if num1>num2:
#     print(num1, 'is greater than',num2)
# elif num1==num2:
#     print(num1, 'is equal to',num2)
# else:
#     print(num2, 'is greater than',num1)

# #6 Print Largest Number among three
# a = int(input("Enter a number: "))
# b = int(input("Enter a number: "))
# c = int(input("Enter a number: "))

# if a>b and a>c:
#     print(a,'is the largest number.')
# elif b>a and b>c:
#     print(b,'is the largest number.')
# elif c>b and c>a:
#     print(c,'is the largest number.')
# else:
#     print('Two or three numbers are equal. Please input different numbers.')

# #7 Make a list of fruits
# basket = []
# while True:
#     fruit = input("Enter the fruit name:")
#     if fruit not in basket:
#         basket.append(fruit)
#         print(fruit,'has been added to the basket.')
#     else:
#         print(fruit,'already added to the basket.')
#     ch = input("Want to add more fruits? (Press Q to Quit): ")
#     if ch=='Q':
#         break
# print('List of fruits: ',basket)

# #8 Divisibility of two numbers
# dividend = int(input("Enter the dividend: "))
# divisor = int(input("Enter the divisor: "))
# print('Quotient = ',dividend/divisor)

# #9 Check age group
# age = int(input('Please enter your age: '))
# if age>=0 and age<=12:
#     print("Ohh! You are a toddler.")
# elif age>=13 and age<=18:
#     print("Ohh! You are a teenager.")
# elif age>=19 and age<=59:
#     print("Ohh! You are a adult.")
# elif age>=60:
#     print("Ohh! You are a senior citizen.")
# else:
#     print("Invalid Age.")

# #10 Check if two variables point to same object
# a = int(input("Enter a number: "))
# b = int(input("Enter a number: "))
# if a is b:
#     print("The variables point to the same object.")
# elif a is not b:
#     print("The variables donot point to the same object.")
# else:
#     print("Invalid choice")

# #11 Organize Logistics
# no_of_items = int(input("Enter number of items: "))
# items_limit = int(input("Enter how many items a box can hold: "))
# print("Number of boxes = ", no_of_items//items_limit)
# print("Leftover items = ", no_of_items%items_limit)

# #12 Check if number is a multiple of 5
# n = int(input("Enter a number: "))
# if n%5==0:
#     print(True)
# else:
#     print(False)

# #13 Check Eligibility
# age = int(input("Enter your age: "))
# height = float(input("Enter your height in cm: "))

#14 Check Loan Eligibility
income = int(input("Enter your monthly income: "))
credit_score = int(input('Enter your credit score: '))
period = int(input("Enter how many years of work experience: "))
if (income>50000 and credit_score>700) or ((income>=30000 and income<=50000) and (credit_score>750 or period>5)):
    print("Congrats! You are eligible to apply for loan.")
elif income<30000:
    print("Sorry! You are ineligible for loan.")