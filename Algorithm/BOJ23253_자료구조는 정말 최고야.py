"""
입력을 받아 각 원소별로 근접한 다른 원소와 크기를 비교해 정렬이 되어있는지 확인하였음
"""
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

is_sorted = True
for m in range(M):
    k = int(input())
    books = list(map(int, input().split()))
    for i in range(1, k):
        if books[i - 1] < books[i]:
            is_sorted = False
            break

print('Yes' if is_sorted else 'No')