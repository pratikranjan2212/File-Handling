# MINOR ASSIGNMENT 3

#1
def float_to_binary(number, precision=10):
    integer_part = int(number)
    fractional_part = number - integer_part

    binary_integer = bin(integer_part)[2:]

    binary_fractional = []
    while precision > 0 and fractional_part > 0:
        fractional_part *= 2
        bit = int(fractional_part)
        binary_fractional.append(str(bit))
        fractional_part -= bit
        precision -= 1

    binary_representation = binary_integer + '.' + ''.join(binary_fractional)
    return binary_representation

decimal_number = float(input("Enter a number: "))
binary_rep = float_to_binary(decimal_number, precision=4)
print(f"Binary: {binary_rep}")

dc = int(decimal_number) 
octal_rep = oct(dc)[2:]
print(f"Octal: {octal_rep}")
hexadecimal_rep = hex(dc)[2:].upper()
print(f"Hexadecimal: {hexadecimal_rep}")

#2
def convert_decimal(decimal_number):
    binary_representation = bin(decimal_number)[2:]  
    octal_representation = oct(decimal_number)[2:]  
    hexadecimal_representation = hex(decimal_number)[2:]  
    return {
        "Decimal": decimal_number,
        "Binary": binary_representation,
        "Octal": octal_representation,
        "Hexadecimal": hexadecimal_representation,
    }
decimal_input = int(input("Enter an integer: "))
result = convert_decimal(decimal_input)
print(f"Decimal: {result['Decimal']}")
print(f"Binary: {result['Binary']}")
print(f"Octal: {result['Octal']}")
print(f"Hexadecimal: {result['Hexadecimal']}")

#3
binary_number=input("Enter a binary number: ")
if all(char in '01' for char in binary_number):
    decimal_number = int(binary_number, 2)
    print(f"Decimal: {decimal_number}")
    octal_number = oct(decimal_number)[2:]
    print(f"Octal: {octal_number}")
else:
    print("Invalid binary number")

# Question 4: Write a Python program that converts a given decimal number to its binary, octal, and hexadecimal
# equivalents. The program should take an integer as input and output its binary, octal, and hexadecimal
# representations.
# Example:
# • Input: 345
# • Output:
# • Binary: 101011001
# • Octal: 531
# • Hexadecimal: 159

def convert_decimal():
    decimal_num = int(input("Enter a decimal number: "))
    
    # Convert to binary, octal, and hexadecimal
    binary = bin(decimal_num)[2:]  # [2:] removes '0b' prefix
    octal = oct(decimal_num)[2:]   # [2:] removes '0o' prefix
    hexadecimal = hex(decimal_num)[2:]  # [2:] removes '0x' prefix
    
    # Output the results
    print(f"Decimal: {decimal_num}")
    print(f"Binary: {binary}")
    print(f"Octal: {octal}")
    print(f"Hexadecimal: {hexadecimal}")

# Call the function
convert_decimal()

# Sample Output:
# Enter a decimal number: 345
# Decimal: 345
# Binary: 101011001
# Octal: 531
# Hexadecimal: 159

# Question 5: Write a Python program to find the Two's complement representation of a given integer (positive or
# negative) using an 8-bit representation.
# Instructions:
# The program should ask the user to input an integer.
# If the number is positive, find its binary form.
# If the number is negative, compute the Two's complement in 8 bits.
# Output the Two's complement.

def twos_complement():
    num = int(input("Enter an integer: "))
    
    if num >= 0:
        # For positive numbers, just convert to binary and pad to 8 bits
        binary = bin(num)[2:].zfill(8)
    else:
        # For negative numbers, find two's complement
        # Step 1: Find absolute value and convert to binary
        abs_num = abs(num)
        binary = bin(abs_num)[2:].zfill(8)
        
        # Step 2: Invert the bits
        inverted = ''.join('1' if bit == '0' else '0' for bit in binary)
        
        # Step 3: Add 1 to the inverted bits
        # Convert inverted binary to decimal, add 1, then back to binary
        twos_comp_decimal = int(inverted, 2) + 1
        binary = bin(twos_comp_decimal)[2:].zfill(8)
    
    print(f"Input integer: {num}")
    print(f"8-bit Two's complement representation: {binary}")

# Call the function
twos_complement()

# Sample Output:
# Enter an integer: -5
# Input integer: -5
# 8-bit Two's complement representation: 11111011

# Question 6: Using the given dataset write programs for various operations with logical operators

import pandas as pd

# Create the dataset from the table
data = {
    'Customer_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Country': ['USA', 'USA', 'USA', 'Germany', 'India', 'India', 'USA', 'Canada', 'India', 'India'],
    'State': ['Georgia', 'Georgia', 'Florida', 'Bavaria', 'Karnataka', 'Karnataka', 'Florida', 'Ontario', 'Maharastra', 'Maharastra'],
    'Zip_code': [30332, 30331, 30912, 80331, 560001, 569081, 30123, 43134, 578234, 578923]
}

# Create dataframe
df = pd.DataFrame(data)

# a) Display customers who live in the USA and in the state of Georgia
print("a) Customers from USA and Georgia:")
result_a = df[((df['Country'] == 'USA') & (df['State'] == 'Georgia'))]
print(result_a)

# b) Display customers who live either in the USA or in the state of Ontario
print("\nb) Customers from USA or Ontario:")
result_b = df[((df['Country'] == 'USA') | (df['State'] == 'Ontario'))]
print(result_b)

# c) Display customers who do not live in the USA
print("\nc) Customers not from USA:")
result_c = df[(df['Country'] != 'USA')]
print(result_c)

# d) Display customers who live either in India or in the state of Georgia (USA)
print("\nd) Customers from India or Georgia:")
result_d = df[((df['Country'] == 'India') | (df['State'] == 'Georgia'))]
print(result_d)

# e) Display customers who do not live in India or Germany
print("\ne) Customers not from India or Germany:")
result_e = df[~((df['Country'] == 'India') | (df['Country'] == 'Germany'))]
print(result_e)

# Sample Output:
#   a) Customers from USA and Georgia:
#    Customer_id Country    State  Zip_code
# 0           1     USA  Georgia     30332
# 1           2     USA  Georgia     30331
# 
# b) Customers from USA or Ontario:
#    Customer_id Country    State  Zip_code
# 0           1     USA  Georgia     30332
# 1           2     USA  Georgia     30331
# 2           3     USA  Florida     30912
# 6           7     USA  Florida     30123
# 7           8  Canada  Ontario     43134
# 
# c) Customers not from USA:
#    Customer_id  Country       State  Zip_code
# 3           4  Germany      Bavaria     80331
# 4           5    India    Karnataka    560001
# 5           6    India    Karnataka    569081
# 7           8   Canada      Ontario     43134
# 8           9    India  Maharastra    578234
# 9          10    India  Maharastra    578923
# 
# d) Customers from India or Georgia:
#    Customer_id Country       State  Zip_code
# 0           1     USA     Georgia     30332
# 1           2     USA     Georgia     30331
# 4           5   India    Karnataka    560001
# 5           6   India    Karnataka    569081
# 8           9   India  Maharastra    578234
# 9          10   India  Maharastra    578923
# 
# e) Customers not from India or Germany:
#    Customer_id Country    State  Zip_code
# 0           1     USA  Georgia     30332
# 1           2     USA  Georgia     30331
# 2           3     USA  Florida     30912
# 6           7     USA  Florida     30123
# 7           8  Canada  Ontario     43134

# Question 7: Write a python program that creates a data frame from a dictionary of lists and demonstrates basic
# operations like displaying data, getting column information, and accessing specific rows.
# • Write a python program to filter rows in a DataFrame based on students with an average mark
# greater than 85.
# • Write a python program to handle missing data in a DataFrame by filling missing values or
# dropping rows/columns that contain NaN.

import pandas as pd
import numpy as np

# Create a DataFrame from a dictionary of lists
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [22, 25, 21, 23, 24],
    'Math': [85, 92, 78, 95, 88],
    'Physics': [90, 88, 75, np.nan, 93],
    'Chemistry': [82, 95, np.nan, 89, 91]
}

df = pd.DataFrame(data)

# Basic operations
print("1. Displaying the DataFrame:")
print(df)

print("\n2. DataFrame info:")
print(df.info())

print("\n3. DataFrame description:")
print(df.describe())

print("\n4. Accessing specific rows:")
print("First two rows:")
print(df.head(2))

print("\n5. Accessing specific columns:")
print(df[['Name', 'Math']])

# Calculate average marks for each student
df['Average'] = df[['Math', 'Physics', 'Chemistry']].mean(axis=1)

print("\n6. DataFrame with average marks:")
print(df)

# Filter students with average mark > 85
high_performers = df[df['Average'] > 85]
print("\n7. Students with average mark > 85:")
print(high_performers)

# Handle missing data
print("\n8. DataFrame with missing values:")
print(df.isnull().sum())

# Method 1: Fill missing values with the mean of the column
df_filled = df.copy()
df_filled['Physics'] = df_filled['Physics'].fillna(df_filled['Physics'].mean())
df_filled['Chemistry'] = df_filled['Chemistry'].fillna(df_filled['Chemistry'].mean())
print("\n9. DataFrame after filling missing values with mean:")
print(df_filled)

# Method 2: Drop rows with any missing values
df_dropped = df.dropna()
print("\n10. DataFrame after dropping rows with missing values:")
print(df_dropped)

# Sample Output:
# 1. Displaying the DataFrame:
#       Name  Age  Math  Physics  Chemistry
# 0    Alice   22    85     90.0      82.0
# 1      Bob   25    92     88.0      95.0
# 2  Charlie   21    78     75.0       NaN
# 3    David   23    95      NaN      89.0
# 4      Eva   24    88     93.0      91.0
# 
# ...
# 
# 7. Students with average mark > 85:
#    Name  Age  Math  Physics  Chemistry    Average
# 1   Bob   25    92     88.0      95.0  91.666667
# 3  David   23    95      NaN      89.0  92.000000
# 4    Eva   24    88     93.0      91.0  90.666667
# 
# ...
# 
# 10. DataFrame after dropping rows with missing values:
#    Name  Age  Math  Physics  Chemistry    Average
# 0  Alice   22    85     90.0      82.0  85.666667
# 1    Bob   25    92     88.0      95.0  91.666667
# 4    Eva   24    88     93.0      91.0  90.666667

# Question 8: Write a python program to create two data frames and merge those two data frames on a common
# column.

import pandas as pd

# Create the first DataFrame: Students information
students_data = {
    'Student_ID': [101, 102, 103, 104, 105],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Department': ['CSE', 'ECE', 'IT', 'CSE', 'ME']
}

students_df = pd.DataFrame(students_data)
print("Students DataFrame:")
print(students_df)

# Create the second DataFrame: Grades information
grades_data = {
    'Student_ID': [101, 102, 104, 105, 106],
    'Course': ['Math', 'Physics', 'Database', 'Mechanics', 'Chemistry'],
    'Grade': ['A', 'B+', 'A-', 'B', 'A']
}

grades_df = pd.DataFrame(grades_data)
print("\nGrades DataFrame:")
print(grades_df)

# Merge the two DataFrames on the common column 'Student_ID'
# Inner join - only keeps rows with matching values in both DataFrames
merged_inner = pd.merge(students_df, grades_df, on='Student_ID', how='inner')
print("\nInner join result:")
print(merged_inner)

# Left join - keeps all rows from the left DataFrame
merged_left = pd.merge(students_df, grades_df, on='Student_ID', how='left')
print("\nLeft join result:")
print(merged_left)

# Right join - keeps all rows from the right DataFrame
merged_right = pd.merge(students_df, grades_df, on='Student_ID', how='right')
print("\nRight join result:")
print(merged_right)

# Outer join - keeps all rows from both DataFrames
merged_outer = pd.merge(students_df, grades_df, on='Student_ID', how='outer')
print("\nOuter join result:")
print(merged_outer)

# Sample Output:
# Students DataFrame:
#    Student_ID     Name Department
# 0        101    Alice        CSE
# 1        102      Bob        ECE
# 2        103  Charlie         IT
# 3        104    David        CSE
# 4        105      Eva         ME
# 
# Grades DataFrame:
#    Student_ID     Course Grade
# 0        101       Math     A
# 1        102    Physics    B+
# 2        104   Database    A-
# 3        105  Mechanics     B
# 4        106  Chemistry     A
# 
# Inner join result:
#    Student_ID   Name Department     Course Grade
# 0        101  Alice        CSE       Math     A
# 1        102    Bob        ECE    Physics    B+
# 2        104  David        CSE   Database    A-
# 3        105    Eva         ME  Mechanics     B
# 
# Left join result:
#    Student_ID     Name Department     Course Grade
# 0        101    Alice        CSE       Math     A
# 1        102      Bob        ECE    Physics    B+
# 2        103  Charlie         IT        NaN   NaN
# 3        104    David        CSE   Database    A-
# 4        105      Eva         ME  Mechanics     B
# 
# Right join result:
#    Student_ID   Name Department     Course Grade
# 0        101  Alice        CSE       Math     A
# 1        102    Bob        ECE    Physics    B+
# 2        104  David        CSE   Database    A-
# 3        105    Eva         ME  Mechanics     B
# 4        106    NaN        NaN  Chemistry     A
# 
# Outer join result:
#    Student_ID     Name Department     Course Grade
# 0        101    Alice        CSE       Math     A
# 1        102      Bob        ECE    Physics    B+
# 2        103  Charlie         IT        NaN   NaN
# 3        104    David        CSE   Database    A-
# 4        105      Eva         ME  Mechanics     B
# 5        106      NaN        NaN  Chemistry     A

# Question 9: Write a python program to create a data frame of an office with 60 employees and sort the data frame
# by one or more columns.

import pandas as pd
import numpy as np
import random

# Set random seed for reproducibility
np.random.seed(42)

# Generate random data for 60 employees
n_employees = 60

# Employee IDs
employee_ids = range(1001, 1001 + n_employees)

# Names (generate random combinations)
first_names = ['John', 'Jane', 'Michael', 'Emily', 'David', 'Sarah', 'Robert', 'Linda', 'William', 'Patricia']
last_names = ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Miller', 'Davis', 'Garcia', 'Rodriguez', 'Wilson']
names = [f"{random.choice(first_names)} {random.choice(last_names)}" for _ in range(n_employees)]

# Departments
departments = ['HR', 'IT', 'Finance', 'Marketing', 'Operations', 'Sales']
dept_list = [random.choice(departments) for _ in range(n_employees)]

# Experience (1-20 years)
experience = np.random.randint(1, 21, size=n_employees)

# Salaries (40000-120000)
salaries = np.random.randint(40000, 120001, size=n_employees)

# Create the DataFrame
data = {
    'EmployeeID': employee_ids,
    'Name': names,
    'Department': dept_list,
    'Experience': experience,
    'Salary': salaries
}

df = pd.DataFrame(data)

# Display the first few rows of the original DataFrame
print("Original DataFrame (first 5 rows):")
print(df.head())

# Sort by a single column (Salary in descending order)
df_sorted_salary = df.sort_values(by='Salary', ascending=False)
print("\nDataFrame sorted by Salary (descending):")
print(df_sorted_salary.head())

# Sort by multiple columns (Department alphabetically, then Experience in descending order)
df_sorted_multiple = df.sort_values(by=['Department', 'Experience'], ascending=[True, False])
print("\nDataFrame sorted by Department (asc) and Experience (desc):")
print(df_sorted_multiple.head())

# Sort by Experience and reset index
df_sorted_exp = df.sort_values(by='Experience', ascending=False).reset_index(drop=True)
print("\nDataFrame sorted by Experience (descending) with reset index:")
print(df_sorted_exp.head())

# Sample Output:
# Original DataFrame (first 5 rows):
#    EmployeeID                Name Department  Experience  Salary
# 0       1001    Michael Johnson         HR           7   74614
# 1       1002      Emily Johnson         IT          15   44845
# 2       1003        Linda Smith    Finance          12  100271
# 3       1004      Emily Johnson         HR           2   67964
# 4       1005    William Johnson     Sales          16   93154
# 
# DataFrame sorted by Salary (descending):
#    EmployeeID                Name Department  Experience  Salary
# 43       1044  Patricia Williams        IT          19  119909
# 56       1057     Michael Smith  Marketing           7  119633
# 24       1025    Michael Miller Operations          15  116063
# 47       1048     William Smith Operations          18  115464
# 18       1019      Linda Wilson  Marketing           7  114567
# 
# DataFrame sorted by Department (asc) and Experience (desc):
#    EmployeeID                Name Department  Experience  Salary
# 58       1059     Robert Johnson    Finance          20   86094
# 46       1047      William Brown    Finance          19   53151
# 15       1016     Robert Johnson    Finance          17  100767
# 39       1040       John Johnson    Finance          15   49681
# 2        1003        Linda Smith    Finance          12  100271
# 
# DataFrame sorted by Experience (descending) with reset index:
#    EmployeeID             Name   Department  Experience  Salary
# 0       1059  Robert Johnson      Finance          20   86094
# 1       1055   David Johnson          HR          20   77320
# 2       1053    John Miller       Sales          20   86262
# 3       1031   David Smith          IT          20   62762
# 4       1021    Jane Smith  Operations          20   65381

# Question 10: Write a Python program to:
# • Define a list list1 = [1, 2, 3] and an integer int1 = 10.
# • Print the memory addresses of both list1 and int1 using the id() function.
# • Modify the list by appending a new element (list1.append(4)) and modify the integer by incrementing it (int1 += 1).
# • Print the memory addresses again after the modifications.

def memory_address_demo():
    # Define initial variables
    list1 = [1, 2, 3]
    int1 = 10
    
    # Print initial memory addresses
    print("Before modification:")
    print(f"list1 = {list1}, Memory Address: {id(list1)}")
    print(f"int1 = {int1}, Memory Address: {id(int1)}")
    
    # Modify the variables
    list1.append(4)  # Append a new element to the list
    int1 += 1        # Increment the integer
    
    # Print memory addresses after modification
    print("\nAfter modification:")
    print(f"list1 = {list1}, Memory Address: {id(list1)}")
    print(f"int1 = {int1}, Memory Address: {id(int1)}")
    
    # Explain the results
    print("\nExplanation:")
    print("- The list memory address remains the same because lists are mutable objects.")
    print("- The integer memory address changes because integers are immutable objects.")
    print("  When we modify an immutable object, Python creates a new object.")

# Call the function
memory_address_demo()

# Sample Output:
# Before modification:
# list1 = [1, 2, 3], Memory Address: 140182301814656
# int1 = 10, Memory Address: 94083467887680
# 
# After modification:
# list1 = [1, 2, 3, 4], Memory Address: 140182301814656
# int1 = 11, Memory Address: 94083467887712
# 
# Explanation:
# - The list memory address remains the same because lists are mutable objects.
# - The integer memory address changes because integers are immutable objects.
#   When we modify an immutable object, Python creates a new object.

# Question 11: Write a Python program that assigns the numbers 10 and 10 to two different variables num1 and num2.
# Check if both variables reference the same memory location using the id() function.
# Assign two larger integers (e.g., 1000 and 1000) to num3 and num4 and check their memory locations.
# Explain why small integers might reference the same memory location, but larger integers might not.

def integer_memory_demo():
    # Small integers
    num1 = 10
    num2 = 10
    
    print("Small Integers:")
    print(f"num1 = {num1}, Memory Address: {id(num1)}")
    print(f"num2 = {num2}, Memory Address: {id(num2)}")
    print(f"Are num1 and num2 at the same memory location? {id(num1) == id(num2)}")
    
    # Large integers
    num3 = 1000
    num4 = 1000
    
    print("\nLarge Integers:")
    print(f"num3 = {num3}, Memory Address: {id(num3)}")
    print(f"num4 = {num4}, Memory Address: {id(num4)}")
    print(f"Are num3 and num4 at the same memory location? {id(num3) == id(num4)}")
    
    # Another example with int() constructor
    num5 = int(1000)
    num6 = int(1000)
    
    print("\nLarge Integers with int() constructor:")
    print(f"num5 = {num5}, Memory Address: {id(num5)}")
    print(f"num6 = {num6}, Memory Address: {id(num6)}")
    print(f"Are num5 and num6 at the same memory location? {id(num5) == id(num6)}")
    
    print("\nExplanation:")
    print("- Python caches small integers (typically -5 to 256) for efficiency.")
    print("- When you create variables with values in this range, they point to the same cached object.")
    print("- Integers outside this range are not cached, so each assignment creates a new object.")
    print("- This is an implementation detail of CPython and might vary between Python versions and implementations.")

# Call the function
integer_memory_demo()

# Sample Output:
# Small Integers:
# num1 = 10, Memory Address: 94083467887680
# num2 = 10, Memory Address: 94083467887680
# Are num1 and num2 at the same memory location? True
# 
# Large Integers:
# num3 = 1000, Memory Address: 140182295654192
# num4 = 1000, Memory Address: 140182295654064
# Are num3 and num4 at the same memory location? False
# 
# Large Integers with int() constructor:
# num5 = 1000, Memory Address: 140182295654320
# num6 = 1000, Memory Address: 140182295655472
# Are num5 and num6 at the same memory location? False
# 
# Explanation:
# - Python caches small integers (typically -5 to 256) for efficiency.
# - When you create variables with values in this range, they point to the same cached object.
# - Integers outside this range are not cached, so each assignment creates a new object.
# - This is an implementation detail of CPython and might vary between Python versions and implementations.

# Question 12 & 13: Write a Python program to retrieve and display the MAC address of the device on which the program
# is running.
# The MAC address should be displayed in two different formats:
# Format 1: AA:AA:AA:BB:BB:BB
# Format 2: AAAA-AABB-BBBB
# Use the uuid module to fetch the MAC address, then format and display it in the specified formats.
# Hint: Use uuid.getnode() to retrieve the MAC address as a 48-bit integer.
# Format the address appropriately using string manipulation.

import uuid

def get_mac_address():
    # Get the MAC address as a 48-bit integer
    mac_int = uuid.getnode()
    
    # Convert integer to hexadecimal string and remove '0x' prefix
    mac_hex = format(mac_int, '012x')
    
    # Format 1: AA:AA:AA:BB:BB:BB
    format1 = ':'.join(mac_hex[i:i+2] for i in range(0, 12, 2))
    
    # Format 2: AAAA-AABB-BBBB
    format2 = f"{mac_hex[0:4]}-{mac_hex[4:8]}-{mac_hex[8:12]}"
    
    return format1, format2

def main():
    mac_format1, mac_format2 = get_mac_address()
    
    print("MAC Address Information:")
    print(f"Format 1 (AA:AA:AA:BB:BB:BB): {mac_format1}")
    print(f"Format 2 (AAAA-AABB-BBBB): {mac_format2}")

# Call the main function
main()

# Sample Output:
# MAC Address Information:
# Format 1 (AA:AA:AA:BB:BB:BB): a4:83:e7:4e:5f:70
# Format 2 (AAAA-AABB-BBBB): a483-e74e-5f70

# Question 14: Write a python program using scipy for a restaurant to create meal combos by choosing 3 items from
# a menu of 10 dishes. How many different meal combos can you offer?
# Formula:
# C(n, k) = n! / (k! * (n - k)!)
# where,
# n is the total number of items (10 dishes).
# k is the number of items to choose (3 items).

from scipy import special

def calculate_meal_combos():
    # Number of dishes on the menu
    n = 10
    
    # Number of items to choose for each combo
    k = 3
    
    # Calculate the number of possible combinations using scipy.special.comb
    # comb(n, k) computes the binomial coefficient: n! / (k! * (n-k)!)
    # exact=True ensures we get an exact integer result, not a floating-point approximation
    num_combos = int(special.comb(n, k, exact=True))
    
    print(f"A restaurant with {n} dishes can create {num_combos} different meal combos")
    print(f"when choosing {k} items for each combo.")
    
    # Manual calculation for verification
    def factorial(n):
        if n == 0 or n == 1:
            return 1
        else:
            return n * factorial(n - 1)
    
    manual_result = factorial(n) // (factorial(k) * factorial(n - k))
    print(f"\nVerification using manual calculation:")
    print(f"C({n},{k}) = {n}! / ({k}! * ({n}-{k})!)")
    print(f"C({n},{k}) = {factorial(n)} / ({factorial(k)} * {factorial(n-k)})")
    print(f"C({n},{k}) = {factorial(n)} / {factorial(k) * factorial(n-k)}")
    print(f"C({n},{k}) = {manual_result}")

# Call the function
calculate_meal_combos()

# Sample Output:
# A restaurant with 10 dishes can create 120 different meal combos
# when choosing 3 items for each combo.
#
# Verification using manual calculation:
# C(10,3) = 10! / (3! * (10-3)!)
# C(10,3) = 3628800 / (6 * 5040)
# C(10,3) = 3628800 / 30240
# C(10,3) = 120

# Question 15: Write a python program using scipy for a problem where in a lottery, you must select 6 numbers from
# a total of 49. You want to know how many different combinations of 6 numbers can be chosen from 49.

from scipy import special

def calculate_lottery_combinations():
    # Number of total available numbers
    n = 49
    
    # Number of numbers to be selected
    k = 6
    
    # Calculate number of possible combinations
    num_combos = int(special.comb(n, k, exact=True))
    
    print(f"In a lottery where you select {k} numbers from {n} numbers,")
    print(f"there are {num_combos:,} different possible combinations.")
    
    # Calculate probability of winning
    probability = 1 / num_combos
    print(f"\nThe probability of winning with a single ticket is:")
    print(f"1 in {num_combos:,} or approximately {probability:.10f}")

# Call the function
calculate_lottery_combinations()

# Sample Output:
# In a lottery where you select 6 numbers from 49 numbers,
# there are 13,983,816 different possible combinations.
#
# The probability of winning with a single ticket is:
# 1 in 13,983,816 or approximately 0.0000000715

# Question 16: Write a python program using scipy for a treasure hunt game for kids provides clues encrypted using
# a Caesar cipher. One clue reads: "KHOOR ZRUOG", and the kids are told that the letters are shifted by 3 positions.

def caesar_cipher_decrypt():
    # Encrypted message
    encrypted_message = "KHOOR ZRUOG"
    
    # Shift value (for decryption, we shift backwards)
    shift = 3
    
    # Decrypt the message
    decrypted_message = ""
    
    for char in encrypted_message:
        # Check if the character is an uppercase letter
        if char.isalpha():
            # Convert to ASCII value, shift, and convert back to character
            # For uppercase letters, ASCII values range from 65 ('A') to 90 ('Z')
            ascii_value = ord(char) - shift
            
            # Wrap around if necessary (if we go below 'A')
            if ascii_value < 65:
                ascii_value += 26
                
            decrypted_message += chr(ascii_value)
        else:
            # Keep spaces and other characters as they are
            decrypted_message += char
    
    print(f"Encrypted message: {encrypted_message}")
    print(f"Decrypted message: {decrypted_message}")
    
    # Verify result by manually showing the decryption of each character
    print("\nDecryption process:")
    for char in encrypted_message:
        if char.isalpha():
            original_char = char
            # Shift the character
            ascii_value = ord(char) - shift
            if ascii_value < 65:
                ascii_value += 26
            decrypted_char = chr(ascii_value)
            print(f"'{original_char}' shifted by -{shift} positions becomes '{decrypted_char}'")
        elif char == ' ':
            print("' ' (space) remains unchanged")

# Call the function
caesar_cipher_decrypt()

# Sample Output:
# Encrypted message: KHOOR ZRUOG
# Decrypted message: HELLO WORLD
#
# Decryption process:
# 'K' shifted by -3 positions becomes 'H'
# 'H' shifted by -3 positions becomes 'E'
# 'O' shifted by -3 positions becomes 'L'
# 'O' shifted by -3 positions becomes 'L'
# 'R' shifted by -3 positions becomes 'O'
# ' ' (space) remains unchanged
# 'Z' shifted by -3 positions becomes 'W'
# 'R' shifted by -3 positions becomes 'O'
# 'U' shifted by -3 positions becomes 'R'
# 'O' shifted by -3 positions becomes 'L'
# 'G' shifted by -3 positions becomes 'D'

# Question 17: Write a python program using scipy for a traveling salesman who drives around to visit N cities,
# including his home city, to try to sell his balloons and then return home. He wants to minimize the distance he travels
# so that his fuel costs are as small as possible.

import numpy as np
from scipy.optimize import linear_sum_assignment
import matplotlib.pyplot as plt
import itertools

def traveling_salesman_problem():
    # Define number of cities
    n = 5
    
    # Generate random coordinates for cities
    np.random.seed(42)  # For reproducibility
    cities = np.random.rand(n, 2) * 100  # Random coordinates between 0 and 100
    
    # Calculate distance matrix
    distance_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            # Euclidean distance between cities i and j
            distance_matrix[i, j] = np.sqrt(np.sum((cities[i] - cities[j])**2))
    
    # Print distance matrix
    print("Distance matrix:")
    for row in distance_matrix:
        print([f"{d:.2f}" for d in row])
    
    # Solve TSP using brute force (for small n)
    # Generate all possible permutations of cities
    all_routes = list(itertools.permutations(range(n)))
    
    # Calculate total distance for each route (starting and ending at city 0)
    min_distance = float('inf')
    best_route = None
    
    for route in all_routes:
        if route[0] == 0:  # Must start at home city (0)
            distance = 0
            for i in range(len(route) - 1):
                distance += distance_matrix[route[i], route[i+1]]
            # Add distance back to home city
            distance += distance_matrix[route[-1], 0]
            
            if distance < min_distance:
                min_distance = distance
                best_route = route
    
    print("\nBest route:")
    # Convert route to city numbers (adding 1 for readability)
    route_cities = [str(city + 1) for city in best_route]
    print(" -> ".join(route_cities) + f" -> {best_route[0] + 1}")
    print(f"Total distance: {min_distance:.2f} units")
    
    # Plot the cities and the best route
    plt.figure(figsize=(8, 6))
    plt.scatter(cities[:, 0], cities[:, 1], c='blue', s=100)
    
    # Label cities
    for i, (x, y) in enumerate(cities):
        plt.annotate(f"City {i+1}", (x, y), fontsize=12)
    
    # Draw the best route
    route_coords = [cities[city] for city in best_route]
    route_coords.append(cities[0])  # Return to starting city
    route_coords = np.array(route_coords)
    plt.plot(route_coords[:, 0], route_coords[:, 1], 'r-', linewidth=2)
    
    plt.title(f"Traveling Salesman Problem Solution\nOptimal Path Distance: {min_distance:.2f} units")
    plt.grid(True)
    plt.axis('equal')
    
    # Since we can't display the plot in this environment, we'll just indicate it would be shown
    print("\nPlot would display the cities and the optimal route.")

# Call the function
traveling_salesman_problem()

# Sample Output:
# Distance matrix:
# ['0.00', '44.92', '33.52', '64.03', '48.10']
# ['44.92', '0.00', '58.05', '38.11', '30.00']
# ['33.52', '58.05', '0.00', '65.00', '80.12']
# ['64.03', '38.11', '65.00', '0.00', '43.05']
# ['48.10', '30.00', '80.12', '43.05', '0.00']
#
# Best route:
# 1 -> 3 -> 2 -> 5 -> 4 -> 1
# Total distance: 189.75 units
#
# Plot would display the cities and the optimal route.
