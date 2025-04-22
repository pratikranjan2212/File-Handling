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

