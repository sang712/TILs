"""
주어진 조건에 맞게 스위칭을 하도록 하였음
스위칭 방법은 1을 더한 뒤 2로 모듈 연산을 하는 방법으로 하였음
출력 방법에 유의하지 않아서 틀린 답을 도출하였음
"""
import sys
input = sys.stdin.readline

N = int(input())
switches = list(map(int, input().split()))

students = int(input())

for _ in range(students):
    gender, number = map(int, input().split())
    if gender == 1:
        i = 1
        while True:
            if i * number - 1 < N:
                switches[i * number - 1] = (switches[i * number - 1] + 1) % 2
                i += 1
            else:
                break
    if gender == 2:
        switches[number - 1] = (switches[number - 1] + 1) % 2
        i = 1
        while True:
            if number + i - 1 < N and number - i - 1 >= 0 and switches[number + i - 1] == switches[number - i - 1]:
                switches[number + i - 1] = (switches[number + i - 1] + 1) % 2
                switches[number - i - 1] = (switches[number - i - 1] + 1) % 2
                i += 1
            else:
                break
j = 0
while j * 20 < N:
    print(*switches[j * 20 : (j + 1) * 20])
    j += 1
    