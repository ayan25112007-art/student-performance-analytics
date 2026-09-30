class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.grades = {}

    def add_grade(self, course, grade):
        self.grades[course] = float(grade)
    
    def calculate_gpa(self):
        if len(self.grades) == 0:
            return 0.0

        total = 0.0
        for course in self.grades:
            total = total + self.grades[course]

        average = total / len(self.grades)
        return round(average, 2)


