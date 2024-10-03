"""
버블정렬을 구현하는 문제를 그냥 요구하는대로 구현하였음
"""
ans = []
for p in range(int(input())):
    t, *students = map(int, input().split())
    changes = 0
    line = []
    for student in students:
        line.append(student)
        i = len(line) - 1
        while i:
            if line[i] >= line[i-1]:
                break
            line[i], line[i-1] = line[i-1], line[i]
            changes += 1
            i -= 1
    ans.append(' '.join(map(str, (t, changes))))
print(*ans, sep='\n')
