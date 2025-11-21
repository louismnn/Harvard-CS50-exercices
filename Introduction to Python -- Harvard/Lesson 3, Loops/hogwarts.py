students = ["Hermione", "Harry", "Ron", "Draco"]
# the square brackets indicate a list

for student in students:
    print(student)

# for the function range() you need to put a number inside
# the solution for this is len() function

for i in range(len(students)):
    print(i + 1, students[i])

# dict() = dictionnary : associate on value with a other
houses = ["Gryffindor", "Gryffindor", "Gryffindor", "Slytherin"]

students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack russel terrier"},
    {"name": "Draco", "house": "Slytherine", "patronus": None}
    ]

for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")