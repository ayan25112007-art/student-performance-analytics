from student import Student
import analytics
import storage
import validator

def main():

    students = storage.load_from_file()

    while True:
        print("\n  Student Performance System ")
        print("1. Add a new student")
        print("2. Enter marks for a Student")
        print("3. View performance Report")
        print("4. Save and exit")

        choice = input("Select an option (1-4): ").strip()

        if choice == "1":
            s_id = validator.get_non_empty_string("Enter student ID: ")
            if s_id in students:
                print("Error: This Student ID already exists")
            else:
                name = validator.get_non_empty_string("Enter Student Name: ")
                students[s_id] = Student(s_id, name)
                print("Success: Student" + name + " added")

        elif choice == "2":
            s_id = validator.get_non_empty_string("Enter Student ID: ")
            if s_id not in students:
                print("Error: Student ID not found")
            else:
                course = validator.get_non_empty_string("Enter Course Name: ")
                grade = validator.get_valid_grade("Enter grade for " + course + " (0-100): ")
                students[s_id].add_grade(course, grade)
                print("Success: Grade added")

        elif choice == "3":
            analytics.print_performance_summary(students)
            class_avg = analytics.calculate_class_average(students)
            print("Overall class average marks: " + str(class_avg))

        elif choice == "4":
            storage.save_to_file(students)
            print("Data saved")
            break

        else:
            print("Erorr: Invalid choice")

if __name__== "__main__":
    main()