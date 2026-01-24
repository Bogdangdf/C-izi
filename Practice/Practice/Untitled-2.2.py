class Student:
    def __init__(self, name, group, average_grade):
        self.name = name
        self.group = group
        self.average_grade = average_grade

    def show_info(self):
        print(self.name, self.group, self.average_grade)


student1 = Student("Іван", "КН-31", 4.2)
student2 = Student("Олена", "КН-31", 4.6)
student3 = Student("Андрій", "КН-32", 3.9)

student1.show_info()
student2.show_info()
student3.show_info()
