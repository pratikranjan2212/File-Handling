#1 Count down to 0
num = int(input("Enter a number: "))
while num>=0:
    print(num)
    num -= 1

#2 Multiplication Table
n = int(input("Enter a number for its table: "))
for i in range(1, 11):
    print(n,'X',i,'=',n*i)

#3 Largest of 5 numbers
i = 0
list1 = []
while i<5:
    num = int(input("Enter 5 numbers: "))
    list1.append(num)
    i+=1
list1.sort()
print("Largest of 5 numbers given is",list1[-1])

n1 = float(input("Enter 5 numbers: "))
for j in range(4):
    n2 = float(input("Enter 5 numbers: "))
    if n2>n1:
        n1 = n2
    
print("Largest of 5 numbers given is",n1)

#4 Squares of numbers upto n
s = int(input("Enter a number upto the last term of squares: "))
i = 1
while i<=s:
    print("Square of ",i,"is",i**2)
    i += 1

#5 Second largest Element in a series of numbers
n = int(input("Enter how many numbers for input: "))
num1 = int(input("Enter a number: "))
sl = 0
for i in range(1,n):
    num2 = int(input("Enter a number: "))
    if num2>num1:
        sl = num1
        num1 = num2

print(f"The second largest number is {sl}")

#6 Diamond Shaped Pattern
h = int(input("Enter number of rows: "))
for i in range(h):
    print(" " * (h - i - 1) + "*" * (2 * i + 1))
for j in range(h - 2, -1, -1): 
    print(" " * (h - j - 1) + "*" * (2 * j + 1))

#7 Remove duplicate elements
lst = [35, 35, 46, 78, 98, 25, 10, 35, 65, 48, 12, 25]
newlst = []
for i in lst:
    if i not in newlst:
        newlst.append(i)
    else:
        print("Duplicate item: ",i)

print(newlst)

#Q8
num = int(input("Enter a number: "))
num_str = str(num)
if num_str == num_str[::-1]:
    print(f"{num} is a palindrome.")
else:
    print(f"{num} is not a palindrome.")

#Q9
n = int(input("Enter the number of elements in the series: "))
total_sum = 0
i = 0
while i < n:
    num = float(input(f"Enter number {i+1}: "))
    total_sum += num
    i += 1
average = total_sum / n
print(f"The average is: {average}")

#Q10
numbers = list(map(int, input("Enter numbers separated by space: ").split()))
is_sorted = True
i = 1
while i < len(numbers):
    if numbers[i] < numbers[i - 1]:
        is_sorted = False
        break
    i += 1
if is_sorted:
    print("The sequence is sorted in ascending order.")
else:
    print("The sequence is not sorted in ascending order.")

#Q11
n = int(input("Enter the size of the square: "))
for i in range(1, n + 1):
    print(str(i) * n)

#Q12
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
result = 0
count = 0
while count < abs(num2):
    result += abs(num1)
    count += 1
if num2 < 0:
    result = -result
print(f"The product of {num1} and {num2} is {result}")

#Q13
N = int(input("Enter a number N: "))
multiple_of_7 = N + 1

while multiple_of_7 % 7 != 0:
    multiple_of_7 += 1
print(f"The smallest multiple of 7 greater than {N} is {multiple_of_7}.")

#Q14
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")
result = string1 + string2
print("The concatenated string is:", result)

#Q15
string = input("Enter a string: ")
last_char = string[-1]
print(f"The last character of the string is: {last_char}")

#Q16
number = int(input("Enter a number: "))
while number >= 10:
    number = sum(int(digit) for digit in str(number))
print(f"The single digit result is: {number}")

#Q17
number = int(input("Enter a number: "))
sum_odd_digits = 0
while number > 0:
    digit = number % 10  
    if digit % 2 != 0:  
        sum_odd_digits += digit
    number //= 10  
print(f"The sum of odd digits is: {sum_odd_digits}")

#Q18
n = int(input("Enter the number of rows for Pascal's Triangle: "))
triangle = []
for i in range(n):
    row = [1] * (i + 1)
    for j in range(1, i):
        row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
    triangle.append(row)
for row in triangle:
    print(" ".join(map(str, row)).center(2 * n))

#Q19
n = int(input("Enter the number of terms in the Fibonacci sequence: "))
a, b = 0, 1
print("Fibonacci sequence:")
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b

#Q20
for num in range(1,21):
    if num > 15:
        break
    if num %5 ==0:
        continue
    print(num)

#Q21
array = list(map(int, input("Enter numbers separated by space: ").split()))
search_number = int(input("Enter the number to search: "))
for num in array:
    if num == search_number:
        print("Number is found")
        break
else:
    print("Number is not found")

#Q22
original_string = input("Enter a string to reverse: ")
reversed_string = " "
for char in original_string:
    reversed_string = char + reversed_string
print("Reversed string: ",reversed_string)

#Q23
string = input("Enter the string: ")
length = 0
for char in string:
    length +=1
print("Length of the string: ",length)

#Q24
while True:
    num = input("Enter a number: ")
    if num.replace('.' , ' ' , 1).isdigit() and num.count('.')<=1:
        number = float(num)
        break
    else:
        pass
print("You enter the number: ", number)

#Q25
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))
print("Enter the elements of the first matrix row by row:")
matrix1 = []
for _ in range(rows):
    matrix1.append(list(map(int, input().split())))
print("Enter the elements of the second matrix row by row:")
matrix2 = []
for _ in range(rows):
    matrix2.append(list(map(int, input().split())))
if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
    raise ValueError("Matrices must have the same dimensions for addition.")
result = []
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(matrix1[i][j] + matrix2[i][j])
    result.append(row)
print("The resulting matrix after addition is:")
for row in result:
    print(" ".join(map(str, row)))

#Q26
rows1 = int(input("Enter the number of rows for the first matrix: "))
cols1 = int(input("Enter the number of columns for the first matrix: "))

rows2 = int(input("Enter the number of rows for the second matrix: "))
cols2 = int(input("Enter the number of columns for the second matrix: "))
if cols1 != rows2:
    raise ValueError("Matrix multiplication not possible: columns of first matrix must equal rows of second matrix.")
print("Enter the elements of the first matrix row by row (space-separated):")
matrix1 = []
for j in range(rows1):
    matrix1.append(list(map(int, input().split())))
    
print("Enter the elements of the second matrix row by row (space-separated):")
matrix2 = []
for j in range(rows2):
    matrix2.append(list(map(int, input().split())))
result = [[0 for j in range(cols2)] for j in range(rows1)]

for i in range(rows1):
    for j in range(cols2):
        for k in range(cols1):
            result[i][j] += matrix1[i][k] * matrix2[k][j]
print("The resulting matrix after multiplication is:")
for row in result:
    print(" ".join(map(str, row)))

#Q27
input_string = input("Enter a string: ")
result = ""
seen = ""
for char in input_string:
    if char not in seen:
        result += char  
        seen += char    
print("String after removing duplicates:", result)

#Q28
input_string = input("Enter a string: ")
if not input_string: 
    print("The string is empty.")
else:
    print("The string is not empty.")

#Q29
input_string = input("Enter a string: ")
result = ""
for char in input_string:
    if not char.isdigit():  
        result += char 
print("String after removing digits:", result)

#Q30
input_string = input("Enter a string: ")
result = ""
words = input_string.split()
for word in words:
    result += word.capitalize() + " "
print("String after capitalizing each word:", result.strip())


    

    
