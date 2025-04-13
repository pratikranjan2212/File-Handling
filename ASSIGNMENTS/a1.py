#1
Mathematics = {"Ana De Armas","Angelina Jolie","Sydney Sweeney","Alexandra Daddario","Josephine Langford"}
Physics = {"Scarlett Johansson","Elizabeth Olsen", "Ana De Armas","Angelina Jolie","Natalie Portman"}

print("Students enrolled in Maths or Physics: ", Mathematics.union(Physics))
print("Students enrolled in Maths and Physics: ", Mathematics.intersection(Physics))
print("Students enrolled in Maths but not in Physics: ", Mathematics.difference(Physics))
print("Students enrolled in Physics but not in Maths: ", Physics.difference(Mathematics))

#2
Set_A = { "Amit", "Bhavna", "Chirag", "Deepak", "Esha", "Farhan"}
Set_B = { "Chirag", "Deepak", "Farhan", "Gaurav", "Harsh" }

print(True) if "Deepak" in Set_A else print(False)
print("All skilled") if Set_A==Set_B else print("All are not skilled")

#3
print("One emplyoee is skilled in both") if Set_A.intersection(Set_B)==True else print ("Skill issue")
print("")

#4
students = {"Asutosh","Ayushman","Mohit","Priya"}
subjects = {"Mathematics","Physics","Computer Science","Economics"}
from itertools import product
enrollments = set(product(students, subjects))
print(enrollments)

#5
from itertools import product
die1 = die2 = {1,2,3,4,5,6}
print("All outcomes of dice:")
print(set(product(die1,die2)))

#6
R1 : {("Anurag","Nitish"),("Priyabrata","Koustav"),("Prateek","Asutosh")}
R2 : {("Priya","Nikita"),("Nikita","Priya"),("Sancheeta","Shreyashree"),("Shreyashree","Sancheeta")}
def ensure_symmetric(relations):
    # Convert the set of tuples to a list for easier manipulation
    relation_list = list(relations)
    
    # Create a set to store the complete symmetric relations
    complete_relations = set()

    # Iterate through each pair in the relation list
    for a, b in relation_list:
        complete_relations.add((a, b))
        complete_relations.add((b, a))
    
    return complete_relations

R1_symmetric = ensure_symmetric(R1)
R2_symmetric = ensure_symmetric(R2)

print("Symmetric R1:", R1_symmetric)
print("Symmetric R2:", R2_symmetric)

#7
genres = {"Fiction", "Non-Fiction", "Mystery", "Science", "Fantasy"}
age_groups = {"Children", "Teen", "Adult"}
relation_R = set()

for genre in {"Fiction", "Fantasy"}:
    relation_R.add((genre, "Children"))

for genre in genres - {"Non-Fiction"}:
    relation_R.add((genre, "Teen"))

for genre in genres:
    relation_R.add((genre, "Adult"))

print("Library Recommendation Relation R:")
for pair in sorted(relation_R):
    print(f"{pair[0]} is recommended for {pair[1]}")

#8
people = {"Alice", "Bob", "Charlie"}
parent_child = {("Alice", "Bob"), ("Bob", "Charlie")}

is_reflexive = True
missing_reflexive_pairs = []

for person in people:
    if (person, person) not in parent_child:
        is_reflexive = False
        missing_reflexive_pairs.append((person, person))

print(f"Is the relation reflexive? {is_reflexive}")
if not is_reflexive:
    print("Missing reflexive pairs:")
    for pair in missing_reflexive_pairs:
        print(pair)
    
    reflexive_relation = parent_child.copy()
    for pair in missing_reflexive_pairs:
        reflexive_relation.add(pair)
    
    print("\nReflexive relation would be:")
    for pair in sorted(reflexive_relation):
        print(pair)

#9
professor_subject = {("Dr. Smith", "Math"), ("Dr. Johnson", "Physics"), ("Dr. Smith", "Physics")}

professors = {}
for prof, _ in professor_subject:
    if prof in professors:
        professors[prof] += 1
    else:
        professors[prof] = 1

is_function = True
professors_with_multiple_subjects = []

for prof, count in professors.items():
    if count > 1:
        is_function = False
        professors_with_multiple_subjects.append(prof)

print(f"Is the relation a function? {is_function}")
if not is_function:
    print("Professors teaching multiple subjects:")
    for prof in professors_with_multiple_subjects:
        subjects = [subj for p, subj in professor_subject if p == prof]
        print(f"{prof}: {subjects}")

#10
flights = {("New York", "London"), ("London", "Paris"), ("Paris", "Berlin"), ("New York", "Paris")}
is_transitive = True
missing_transitive_pairs = []

for city1, city2 in flights:
    for city3 in [dest for src, dest in flights if src == city2]:
        if (city1, city3) not in flights:
            is_transitive = False
            missing_transitive_pairs.append((city1, city2, city3))

print(f"Is the flight network transitive? {is_transitive}")
if not is_transitive:
    print("Missing transitive connections:")
    for city1, city2, city3 in missing_transitive_pairs:
        print(f"There's a flight from {city1} to {city2} and from {city2} to {city3}, but no direct flight from {city1} to {city3}")
    
    transitive_relation = flights.copy()
    for city1, _, city3 in missing_transitive_pairs:
        transitive_relation.add((city1, city3))
    
    print("\nTransitive relation would include these additional flights:")
    for pair in sorted(transitive_relation - flights):
        print(f"{pair[0]} to {pair[1]}")

#11
supervision = {("Alice", "Bob"), ("Alice", "Charlie"), ("Bob", "David")}
is_anti_symmetric = True
violating_pairs = []

for a, b in supervision:
    if a != b and (b, a) in supervision:
        is_anti_symmetric = False
        violating_pairs.append((a, b))

print(f"Is the supervision relation anti-symmetric? {is_anti_symmetric}")
if not is_anti_symmetric:
    print("Pairs violating anti-symmetry:")
    for a, b in violating_pairs:
        print(f"{a} supervises {b} and {b} supervises {a}")

#12
coding_club = 120  # |A|
robotics_club = 95  # |B|
ai_club = 80  # |C|

coding_robotics = 30  # |A ∩ B|
robotics_ai = 25  # |B ∩ C|
coding_ai = 20  # |A ∩ C|

all_three = 10  # |A ∩ B ∩ C|

total_unique_students = (
    coding_club + robotics_club + ai_club 
    - coding_robotics - robotics_ai - coding_ai 
    + all_three
)

print(f"Total number of unique students in at least one club: {total_unique_students}")

#13
music_drama = 40  # |M ∩ D|
all_three = 15    # |M ∩ D ∩ N|

total_music_drama = music_drama

print(f"Total students in both Music and Drama clubs: {total_music_drama}")

#14
prerequisite_courses = {"Math-101", "Physics-101", "CS-101", "Statistics-101"}
advanced_courses = {"Machine Learning", "Quantum Computing", "Data Science", "Computer Vision", "AI Ethics"}

relation_R = set()

for course in ["Machine Learning", "Data Science"]:
    relation_R.add(("Math-101", course))
    relation_R.add(("Statistics-101", course))

relation_R.add(("Math-101", "Quantum Computing"))
relation_R.add(("Physics-101", "Quantum Computing"))

relation_R.add(("CS-101", "Computer Vision"))
relation_R.add(("Math-101", "Computer Vision"))

for prereq in prerequisite_courses:
    relation_R.add((prereq, "AI Ethics"))

print("Complete Relation R (prerequisite course, advanced course):")
for prereq, adv_course in sorted(relation_R):
    print(f"({prereq}, {adv_course})")

#15
birth_month = {("Neha", "Vikas"), ("Vikas", "Neha"), ("Vikas", "Raj"), ("Raj", "Vikas"), ("Neha", "Raj")}

employees = set()
for a, b in birth_month:
    employees.add(a)
    employees.add(b)

is_reflexive = True
for employee in employees:
    if (employee, employee) not in birth_month:
        is_reflexive = False
        break

is_symmetric = True
for a, b in birth_month:
    if (b, a) not in birth_month:
        is_symmetric = False
        break

is_transitive = True
for a, b in birth_month:
    for c in employees:
        if (b, c) in birth_month and (a, c) not in birth_month:
            is_transitive = False
            break

is_equivalence = is_reflexive and is_symmetric and is_transitive

print(f"Employees: {employees}")
print(f"Is the relation reflexive? {is_reflexive}")
print(f"Is the relation symmetric? {is_symmetric}")
print(f"Is the relation transitive? {is_transitive}")
print(f"Is the relation an equivalence relation? {is_equivalence}")

#16
people_pin_codes = {
    "Alice": "12345",
    "Bob": "12345",
    "Charlie": "67890",
    "David": "67890",
    "Eve": "12345"
}

neighbor_relation = set()
for person1 in people_pin_codes:
    for person2 in people_pin_codes:
        if people_pin_codes[person1] == people_pin_codes[person2]:
            neighbor_relation.add((person1, person2))

is_reflexive = True
for person in people_pin_codes:
    if (person, person) not in neighbor_relation:
        is_reflexive = False
        break

is_symmetric = True
for person1, person2 in neighbor_relation:
    if (person2, person1) not in neighbor_relation:
        is_symmetric = False
        break

print("Neighbor relation (based on same PIN code):")
for pair in sorted(neighbor_relation):
    print(pair)

print(f"\na) Is the relation reflexive? {is_reflexive}")
print(f"b) Is the relation symmetric? {is_symmetric}")

#17
people_pin_codes = {
    "Alice": "12345",
    "Bob": "12345",
    "Charlie": "67890",
    "David": "67890",
    "Eve": "12345"
}

neighbor_relation = set()
for person1 in people_pin_codes:
    for person2 in people_pin_codes:
        if people_pin_codes[person1] == people_pin_codes[person2]:
            neighbor_relation.add((person1, person2))

is_transitive = True
for a, b in neighbor_relation:
    for c in people_pin_codes:
        if (b, c) in neighbor_relation and (a, c) not in neighbor_relation:
            is_transitive = False
            print(f"Transitivity violation: {a} is related to {b}, {b} is related to {c}, but {a} is not related to {c}")
            break
    if not is_transitive:
        break

print(f"Is the neighbor relation transitive? {is_transitive}")

#18
import matplotlib.pyplot as plt
from matplotlib_venn import venn2

cricket = 40
football = 35
both = 15

only_cricket = cricket - both
only_football = football - both

plt.figure(figsize=(10, 6))
venn = venn2(subsets=(only_cricket, only_football, both), 
             set_labels=('Cricket', 'Football'))

venn.get_label_by_id('10').set_text(f'{only_cricket}')
venn.get_label_by_id('01').set_text(f'{only_football}')
venn.get_label_by_id('11').set_text(f'{both}')

plt.title('Survey of Students Playing Cricket and Football')
plt.savefig('sports_survey.png')
plt.show()

#19
import matplotlib.pyplot as plt
from matplotlib_venn import venn3

math = 30
science = 25
english = 20
math_science = 10
science_english = 8
math_english = 7
all_three = 5

subsets = (
    math - math_science - math_english + all_three,  
    science - math_science - science_english + all_three,  
    math_science - all_three,  
    english - math_english - science_english + all_three,  
    math_english - all_three,  
    science_english - all_three, 
    all_three 
)

plt.figure(figsize=(10, 6))
venn = venn3(subsets=subsets, set_labels=('Mathematics', 'Science', 'English'))

plt.title('Survey of Students\' Subject Preferences')
plt.savefig('subject_preferences.png')
plt.show()

#20
import matplotlib.pyplot as plt
from matplotlib_venn import venn2

hindi = 50
english = 40
both = 20

only_hindi = hindi - both
only_english = english - both

plt.figure(figsize=(10, 6))
venn = venn2(subsets=(only_hindi, only_english, both), 
             set_labels=('Hindi', 'English'))

venn.get_label_by_id('10').set_text(f'{only_hindi}')
venn.get_label_by_id('01').set_text(f'{only_english}')
venn.get_label_by_id('11').set_text(f'{both}')

plt.title('Survey of Students\' Language Knowledge')
plt.savefig('language_survey.png')
plt.show()