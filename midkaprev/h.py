n = int(input())
nameOfStudents = list(input().split())
nCurrent = int(input())
nameOfCurrentStudents = list(input().split())
print('Missed students:')
for student in nameOfStudents:
    if student not in nameOfCurrentStudents:
        print('- ', student)

print('Not in the group:')        
for student in nameOfCurrentStudents:
    if student not in nameOfStudents:
        print('- ', student)        
