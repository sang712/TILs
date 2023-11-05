"""
각 연도별, 반 별 인원을 리스트 자료 구조를 이용해 체크하였고
2명 이상인 경우만 따로 set 자료 구조에 저장해 인원 수를 카운팅 하도록 하였음
그 후에 각 학생 별로 몇명의 학생과 같은 반을 했는지 set 자료 구조의 길이를 계산해서
최대를 갖는 학생의 번호를 출력하였음
"""
n = int(input())

classes = [[[] for _ in range(10)] for _ in range(5)]
students = [set() for _ in range(n + 1)]
for i in range(1, n + 1):
    student = list(map(int, input().split()))
    for year, num_class in enumerate(student):
        classes[year][num_class].append(i)

for year in classes:
    for num_class in year:
        if len(num_class) > 1:
            for student in num_class:
                students[student].update(num_class)

max_student = 0
ans = 1
for num, student in enumerate(students):
    if len(student) > max_student:
        max_student = len(student)
        ans = num

print(ans)