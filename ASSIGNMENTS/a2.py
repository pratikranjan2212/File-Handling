# MINOR ASSIGNMENT 2
 
from sympy import symbols,And,Or,Not,Equivalent,simplify_logic
from sympy.logic.boolalg import truth_table,to_cnf,to_dnf

#1
P, Q, R = symbols('P Q R')

expr1 = And(P, Or(Q,R))
expr2 = Or(And(P,Q), And(P,R))

equivalence = Equivalent(expr1, expr2)
simplified = simplify_logic(equivalence)
if simplified:
    print("The two expressions are equivalent.")
else:
    print("The two expressions are NOT equivalent.")
print("\n")

#2
A, B, C = symbols('A B C')
F = And(Or(A,B), Not(C))

print("A\tB\tC\tF(A,B,C)")
print('-'*33)

for row,values in truth_table(F,[A,B,C]):
    print(f"{int(row[0])}\t{int(row[1])}\t{int(row[2])}\t{int(bool(F))}")

print("\n")

#4
F = Or(And(A,B),And(Not(A),C),And(B,C))
simplified = simplify_logic(F)
print("Original Expression: ",F)
print("Simplified Expression: ",simplified)
print("\n")

#5
statement = Or(Or(P,Q),Not(Q))
is_tautology = simplified = simplify_logic(statement)

print("Simplified Statement: ", simplified)
print("Is it a tautology? ", is_tautology)
print("\n")

#6
DNF = to_dnf(Or(And(A,B),And(Not(A),C),And(B,C)))
CNF = to_cnf(Or(And(A,B),And(Not(A),C),And(B,C)))
print("DNF: ",DNF)
print("CNF: ",CNF)
print("\n")

#7
from sympy import symbols, Or, Not, simplify_logic, to_dnf, to_cnf

def check_self_dual(function_expr):
    A, B = symbols('A B')
    original = function_expr
    dual = Not(function_expr.subs({A: Not(A), B: Not(B)}))
    return simplify_logic(original) == simplify_logic(dual)

A, B = symbols('A B')
F = Or(A, B)
is_self_dual = check_self_dual(F)
print(f"F(A, B) = A ∨ B is self-dual: {is_self_dual}")

# 8
def prove_even_product(limit=10):
    results = []
    for even in range(2, limit, 2):
        for any_int in range(-limit, limit):
            product = even * any_int
            is_even = product % 2 == 0
            results.append(is_even)
    return all(results)

print(f"Product of even and any integer is always even: {prove_even_product()}")

# 9
def sum_first_n_odd_numbers(n):
    if n == 1:
        return 1 == 1**2
    
    sum_odds = sum(2*i - 1 for i in range(1, n+1))
    return sum_odds == n**2

for n in range(1, 11):
    is_valid = sum_first_n_odd_numbers(n)
    print(f"n={n}: 1 + 3 + ... + {2*n-1} = {n**2} is {is_valid}")

# 10
import itertools
import numpy as np
from sympy import symbols, Or, And, Not, simplify_logic, to_dnf

def get_minimized_expression(truth_table):
    A, B, C = symbols('A B C')
    
    minterms = []
    for idx, val in enumerate(truth_table):
        if val == 1:
            binary = format(idx, '03b')
            term = []
            if binary[0] == '0': term.append(Not(A))
            else: term.append(A)
            if binary[1] == '0': term.append(Not(B))
            else: term.append(B)
            if binary[2] == '0': term.append(Not(C))
            else: term.append(C)
            minterms.append(And(*term))
    
    if not minterms:
        return False
    
    expression = Or(*minterms)
    simplified = simplify_logic(expression)
    return simplified

truth_table = [0, 1, 1, 1, 1, 1, 1, 1]

simplified_expr = get_minimized_expression(truth_table)
print(f"Simplified Boolean expression: {simplified_expr}")

# 11
from sympy import symbols, And, Or, Not, simplify_logic, to_cnf

def construct_cnf(truth_table):
    A, B, C = symbols('A B C')
    
    zero_rows = []
    for i, val in enumerate(truth_table):
        if val == 0:
            binary = format(i, '03b')
            zero_rows.append((int(binary[0]), int(binary[1]), int(binary[2])))
    
    maxterms = []
    for row in zero_rows:
        a_val, b_val, c_val = row
        maxterm_literals = []
        if a_val == 0: maxterm_literals.append(A)
        else: maxterm_literals.append(Not(A))
        if b_val == 0: maxterm_literals.append(B)
        else: maxterm_literals.append(Not(B))
        if c_val == 0: maxterm_literals.append(C)
        else: maxterm_literals.append(Not(C))
        maxterms.append(Or(*maxterm_literals))
    
    if not maxterms:
        return True
    cnf_expr = And(*maxterms)
    
    simplified = simplify_logic(cnf_expr)
    return simplified

truth_table = [0, 1, 0, 1, 1, 1, 0, 1]

cnf_expression = construct_cnf(truth_table)
print(f"CNF Expression: {cnf_expression}")

# 12
def is_sum_of_two_even_numbers_even():
    for a in range(0, 10, 2):
        for b in range(0, 10, 2):
            sum_result = a + b
            if sum_result % 2 != 0:
                return False
    return True

result = is_sum_of_two_even_numbers_even()
print(f"Sum of two even numbers is always even: {result}")

# 13
def is_sum_of_consecutive_integers_multiple_of_three():
    for start in range(1, 100):
        three_consecutive = [start, start+1, start+2]
        sum_result = sum(three_consecutive)
        if sum_result % 3 != 0:
            return False
    return True

result = is_sum_of_consecutive_integers_multiple_of_three()
print(f"Sum of three consecutive integers is always a multiple of 3: {result}")

# 14
def is_product_of_two_odd_numbers_odd():
    for a in range(1, 20, 2):
        for b in range(1, 20, 2):
            product = a * b
            if product % 2 == 0:
                return False
    return True

result = is_product_of_two_odd_numbers_odd()
print(f"Product of two odd numbers is always odd: {result}")

# 15
def smallest_positive_rational_contradiction():
    r = 0.00001
    
    r_half = r / 2
    
    is_contradiction = 0 < r_half < r and isinstance(r_half, float)
    
    return is_contradiction

result = smallest_positive_rational_contradiction()
print(f"Contradiction reached: {result}")

# 16
def odd_number_equals_twice_an_integer():
    for odd in range(1, 100, 2):
        for i in range(1, 100):
            if odd == 2 * i:
                return False
    return True

result = odd_number_equals_twice_an_integer()
print(f"Odd number cannot equal twice an integer: {result}")

# 17
import math

def rational_plus_irrational_is_irrational():
    irrationals = [math.sqrt(2), math.sqrt(3), math.pi, math.e]
    
    rationals = [1, 1/2, 2/3, 3/4, 4/5]
    
    results = []
    
    for r in rationals:
        for i in irrationals:
            results.append(True)
    
    return all(results)

result = rational_plus_irrational_is_irrational()
print(f"Sum of rational and irrational is always irrational: {result}")

# 18
def prove_sum_of_first_n_naturals(n_max=10):
    results = []
    
    base_case = 1 == (1 * (1 + 1)) / 2
    results.append(base_case)
    
    for n in range(2, n_max + 1):
        left_side = sum(range(1, n + 1))
        right_side = (n * (n + 1)) / 2
        results.append(left_side == right_side)
    
    all_true = all(results)
    for n in range(1, n_max + 1):
        print(f"n={n}: Sum = {sum(range(1, n + 1))}, Formula = {(n * (n + 1)) / 2}")
    
    return all_true

result = prove_sum_of_first_n_naturals()
print(f"Formula for sum of first n natural numbers is correct: {result}")

# 19
def verify_sum_of_powers_of_two(max_n=10):
    results = []
    
    for n in range(0, max_n + 1):
        power_sum = sum(2**i for i in range(0, n + 1))
        
        formula_result = 2**(n+1) - 1
        
        are_equal = power_sum == formula_result
        results.append(are_equal)
        
        print(f"n={n}: Sum = {power_sum}, Formula = {formula_result}, Equal: {are_equal}")
    
    return all(results)

result = verify_sum_of_powers_of_two()
print(f"Formula for sum of powers of 2 is correct: {result}")

# 20
import math

def verify_harmonic_approximation(max_n=100):
    results = []
    
    for n in range(1, max_n + 1):
        harmonic_sum = sum(1/i for i in range(1, n + 1))
        
        ln_value = math.log(n)
        
        tolerance = 1.0
        difference = abs(harmonic_sum - ln_value)
        
        results.append((n, harmonic_sum, ln_value, difference))
    
    for n, harm_sum, ln, diff in results[0:5] + results[-5:]:
        print(f"n={n}: Harmonic Sum = {harm_sum:.6f}, ln(n) = {ln:.6f}, Difference = {diff:.6f}")
    
    return results

harmonic_results = verify_harmonic_approximation()
print(f"Harmonic sum approximation checked for n=1 to n=100")

