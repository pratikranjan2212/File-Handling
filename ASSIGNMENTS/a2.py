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

