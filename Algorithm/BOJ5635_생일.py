"""
생일 순으로 정렬하여 문제를 풀이하였음
"""
import sys
input = sys.stdin.readline

N = int(input())

students = []
for _ in range(N):
    name, *birthday = input().split()
    students.append((name, *(map(int, birthday))))
    
students.sort(key=lambda x: (x[3], x[2], x[1]))
print(students[-1][0])
print(students[0][0])