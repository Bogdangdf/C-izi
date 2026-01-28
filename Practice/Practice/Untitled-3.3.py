students = {}

n = int(input())

for i in range(n):
    name = input()
    grades = list(map(float, input().split()))
    students[name] = grades

average_grades = {}
unique_grades = set()

for name, grades in students.items():
    avg = sum(grades) / len(grades)
    average_grades[name] = avg
    for g in grades:
        unique_grades.add(g)

print(average_grades)
print(unique_grades)
