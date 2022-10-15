import sys
input = sys.stdin.readline

students = set(i for i in range(1, 31))
assigned = set()

for _ in range(28):
    assigned.add(int(input()))

culprit = list(students-assigned)
culprit.sort()
for student in culprit:
    print(student)