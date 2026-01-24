students = {}

n = int(input())

i = 0
while i < n:
    name = input()
    grades = list(map(float, input().split()))
    students[name] = grades
    i += 1

averages = {}
unique_grades = set()

for name, grades in students.items():
    avg = sum(grades) / len(grades)
    averages[name] = avg
    for g in grades:
        unique_grades.add(g)

print(averages)
print(sum(averages.values()) / len(averages))
print(unique_grades)
