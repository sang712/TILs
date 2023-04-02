"""
문제에서 요구하는대로 구현하였음
M번을 반복하면서 입력을 받는 대로 i부터 j까지 반복하면서 공을 새롭게 넣고
마지막에 출력하는 방식으로 구현하였음
"""
import sys
input = sys.stdin.readline
N, M = map(int, input().split())

basket = [0] * N

for _ in range(M):
    i, j, k = map(int, input().split())
    for idx in range(i - 1, j):
        basket[idx] = k

print(*basket)