def calculate_class_average(student_dict):
    if len(student_dict) == 0:
        return 0.0

    total_gpa = 0.0
    for s_id in student_dict:
        student_object = student_dict[s_id]
        total_gpa = total_gpa + student_object.calculate_gpa()

    class_average = total_gpa / len(student_dict)
    return round(class_average, 2)

def print_performance_summary(student_dict):
    if len(student_dict) == 0:
        print("no student data record")
        return

    print("\n Class Performance Summary ")
    for s_id in student_dict:
        student_object = student_dict[s_id]
        gpa = student_object.calculate_gpa()
        print("ID: " + s_id + "| Name: " + student_object.name + "| GPA: " + str(gpa))