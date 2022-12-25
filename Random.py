N = int(input())
students = []
for i in range(N):
    name = input()
    score = float(input())
    students.append([name, score])
sorted_students = sorted(students, key=lambda x: x[1], reverse=True)
print(sorted_students)

for i in range(N-3):
    if sorted_students[i][1] >= sorted_students[i+1][1]:
        sorted_students.pop(i)
print(sorted_students)

""" 5
sajid
2.84
umam
2.84
mahabub
2.94
masud
2.94
latif
2.84 """
