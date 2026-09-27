class Student:
    def __init__(self,name,student_id,course,age):
        self.name = name
        self.student_id = student_id
        self.course = course
        self.age = int(age)
    def show(self):
        print("Name :",self.name)
        print("Student ID :",self.student_id)
        print("Course :",self.course)
        print("Age :",self.age)

def read_students(filename):
    students = []
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line == "":
                continue
            student_id, name, course, age = line.split(",")
            students.append(Student(name, student_id, course, age))
    return students

def show_young_students():
    i = 0
    young_students = 1000
    while i < len(students):
        if students[i].age < young_students:
            young_students = students[i].age
        i += 1
    return young_students


students = read_students("stu_data.txt")
print("Youngest student age is:", show_young_students())


            

    