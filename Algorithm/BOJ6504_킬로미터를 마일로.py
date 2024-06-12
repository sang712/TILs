"""
시간 단축을 위해 피보나치수를 구해서 그 값으로 초기화 하였고
구한 피보나치수를 역순으로 돌면서 마일로 변환하는 작업을 진행 했음

피보나치 수의 비율이 1.6에 수렴하고
킬로-마일 변환이 1.6이어서 가능한 문제인 것으로 생각됨
"""
import sys
input = sys.stdin.readline

fibo = [1, 2, 3, 5, 8, 
        13, 21, 34, 55, 89, 
        144, 233, 377, 610, 987, 
        1597, 2584, 4181, 6765, 10946, 17711]

for t in range(int(input())):
    kilo = int(input())
    mile = 0
    for i in range(len(fibo)-1, 0, -1):
        if kilo >= fibo[i]:
            kilo -= fibo[i]
            mile += fibo[i-1]
    print(mile)