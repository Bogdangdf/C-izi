class Student:
    def __init__(self, name, group, average_grade):
        self.name = name
        self.group = group
        self.average_grade = average_grade

    def show_info(self):
        print(self.name, self.group, self.average_grade)


s1 = Student("Іван", "КН-31", 4.3)
s2 = Student("Олена", "КН-31", 4.7)
s3 = Student("Андрій", "КН-32", 3.9)

s1.show_info()
s2.show_info()
s3.show_info()
