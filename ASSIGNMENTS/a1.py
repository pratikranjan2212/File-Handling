# #1
# Mathematics = {"Ana De Armas","Angelina Jolie","Sydney Sweeney","Alexandra Daddario","Josephine Langford"}
# Physics = {"Scarlett Johansson","Elizabeth Olsen", "Ana De Armas","Angelina Jolie","Natalie Portman"}

# print("Students enrolled in Maths or Physics: ", Mathematics.union(Physics))
# print("Students enrolled in Maths and Physics: ", Mathematics.intersection(Physics))
# print("Students enrolled in Maths but not in Physics: ", Mathematics.difference(Physics))
# print("Students enrolled in Physics but not in Maths: ", Physics.difference(Mathematics))

# #2
# Set_A = { "Amit", "Bhavna", "Chirag", "Deepak", "Esha", "Farhan"}
# Set_B = { "Chirag", "Deepak", "Farhan", "Gaurav", "Harsh" }

# print(True) if "Deepak" in Set_A else print(False)
# print("All skilled") if Set_A==Set_B else print("All are not skilled")

# #3
# print("One emplyoee is skilled in both") if Set_A.intersection(Set_B)==True else print ("Skill issue")
# print("")

# #4
# students = {"Asutosh","Ayushman","Mohit","Priya"}
# subjects = {"Mathematics","Physics","Computer Science","Economics"}
# from itertools import product
# enrollments = set(product(students, subjects))
# print(enrollments)

# #5
# from itertools import product
# die1 = die2 = {1,2,3,4,5,6}
# print("All outcomes of dice:")
# print(set(product(die1,die2)))

# #6
# R1 : {("Anurag","Nitish"),("Priyabrata","Koustav"),("Prateek","Asutosh")}
# R2 : {("Priya","Nikita"),("Nikita","Priya"),("Sancheeta","Shreyashree"),("Shreyashree","Sancheeta")}
# def ensure_symmetric(relations):
#     # Convert the set of tuples to a list for easier manipulation
#     relation_list = list(relations)
    
#     # Create a set to store the complete symmetric relations
#     complete_relations = set()

#     # Iterate through each pair in the relation list
#     for a, b in relation_list:
#         complete_relations.add((a, b))
#         complete_relations.add((b, a))
    
#     return complete_relations

# R1_symmetric = ensure_symmetric(R1)
# R2_symmetric = ensure_symmetric(R2)

# print("Symmetric R1:", R1_symmetric)
# print("Symmetric R2:", R2_symmetric)

#7
Genres = { "Fiction", "Non-Fiction", "Mystery", "Science", "Fantasy" }
AgeGroup = { "Children", "Teen", "Adult" }

