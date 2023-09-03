
# Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
# Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

student_data = []
for _ in range(int(input())):
    name = input()
    grade = float(input())
    student_data.append([name, grade])

# Sort the list by grades in ascending order
sorted_data = sorted(student_data, key=lambda x: x[1])

# Find the second lowest grade
second_lowest_grade = None
for i in range(1, len(sorted_data)):
    if sorted_data[i][1] != sorted_data[i - 1][1]:
        second_lowest_grade = sorted_data[i][1]
        break

# Collect the names of students with the second lowest grade
second_lowest_names = []
for name, grade in sorted_data:
    if grade == second_lowest_grade:
        second_lowest_names.append(name)

# Sort the collected names alphabetically
second_lowest_names.sort()

# Print each name on a new line
for name in second_lowest_names:
    print(name)
