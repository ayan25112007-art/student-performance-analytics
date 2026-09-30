from student import Student

def save_to_file(student_dict, filename="students.txt"):

    file = open(filename, "w")

    for s_id in student_dict:
        student = student_dict[s_id]

        file.write("Student,"  + s_id + "," + student.name + "\n")

        for course in student.grades:
            grade = student.grades[course]
            file.write("Grade," + s_id + "," + course + "," + str(grade) + "\n")

    file.close()
    print("[System]: Data successfully saved to " + filename)

def load_from_file(filename="students.txt"):
    student_dict = {}
    try:
        file = open(filename, "r")
        lines = file.readlines()
        file.close()


        for line in lines:
            parts = line.strip().split(",")
            if parts[0] == "Student":
                s_id = parts[1]
                name = parts[2]
                student_dict[s_id] = Student(s_id, name)


        for line in lines:
            parts = line.strip().split(",")
            if parts[0] == "Grade":
                s_id = parts[1]
                course = parts[2]
                grade = float(parts[3])
                if s_id in student_dict:
                    student_dict[s_id].add_grade(course, grade)
    except:
        print("[System]: No data found, Starting")

    return student_dict