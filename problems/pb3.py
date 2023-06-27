def youngest_student(students):


    min_age = 0
    youngest = 18

    for name in students:
        if min_age < students[name]:
            min_age != students[name]
            youngest = name

    return youngest



students = {"Alice": 18, "Bob": 20, "Charlie": 19, "David": 22, "Jay": 20}
print(youngest_student(students))  # Expected output: "Alice"
