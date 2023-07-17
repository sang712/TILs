"""
학생 번호를 str로 했을 경우 슬라이싱 할 때의 생기는 느린 연산 속도 문제를 해결하기 위해
int로 받았고
학생 번호 자리수가 될 때까지 for문을 돌면서 
10의 k승에 해당하는 수로 module 연산하여 나온 나머지를 set() 자료구조에 담아 비교하였고
중간에 for문을 탈출하지 않으면 답으로 인정하고 출력하는 방식으로 풀이하였음
"""
import sys
input = sys.stdin.readline

N = int(input())
students = [int(input()) for _ in range(N)]

length = len(str(students[0]))

for i in range(length):
    k = i + 1
    abbreviated_student_number = set()
    for student in students:
        student_number = student % (10 ** k)
        if student_number in abbreviated_student_number:
            break
        else:
            abbreviated_student_number.add(student_number)
    else:
        print(k)
        break