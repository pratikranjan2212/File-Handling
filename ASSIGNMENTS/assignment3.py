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
# print("Ok")

# #14 Check Loan Eligibility
# income = int(input("Enter your monthly income: "))
# credit_score = int(input('Enter your credit score: '))
# period = int(input("Enter how many years of work experience: "))
# if (income>50000 and credit_score>700) or ((income>=30000 and income<=50000) and (credit_score>750 or period>5)):
#     print("Congrats! You are eligible to apply for loan.")
# elif income<30000:
#     print("Sorry! You are ineligible for loan.")
# else:
#     print("Sorry! You are ineligible for loan.")

# #15 Word categorization
# word = input("Enter a word: ")
# if len(word)<4:
#     print("Short")
# elif len(word)>4 and len(word)<=7:
#     print("Medium")
# else:
#     print("Long")

# #16 Comparing Sum of Digits
# num1 = input("Enter a number: ")
# num2 = input("Enter a number: ")
# l1 = list(num1)
# l2 = list(num2)
# sum1 = 0
# sum2 = 0
# for i, j in zip(l1, l2):
#     sum1 += int(i)
#     sum2 += int(j)

# if sum1>sum2:
#     print("The sum of digits of",num1,"is greater than that of",num2)
# elif sum1<sum2:
#     print("The sum of digits of",num2,"is greater than that of",num1)
# else:
#     print("The sum of digits in both the numbers are equal.")

#17 Date Representation
day = int(input("Enter a day (1-31): "))
month = int(input("Enter a month (1-12): "))
year = int(input("Enter a year (1500 BC - 2898 AD): "))
month_31days = [1,3,5,7,8,10,12]
month_30days = [4,6,9,11]

def Date_Check():
    if (day>0 and day<=31) and (month>=1 and month <=12) and (year>=1500 and year<=2898):
        if month==2 and day<=28:
            print("Valid Date")
        elif (year%400==0 or (year%4==0 and year%100!=0)):
            if (month==2 and day>29):
                print("Invalid Date")
            else:
                print("Valid Date")
        elif (day==31):
            if month in month_31days:
                print("Valid Date")
            else:
                print("Invalid Date")
        elif (day==30):
            if month in month_30days:
                print("Valid Date")
            else:
                print("Invalid Date")
        else:
            print("Valid Date")
    else:
        print("Invalid Date")
    
Date_Check()
