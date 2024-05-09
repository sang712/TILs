"""
A와 B를 입력받아 각각 정렬하고 A의 원소인 a에 해당 하는 수보다 
작은 B의 원소 b의 수가 몇 개 있는지 이분탐색으로 탐색한 뒤에 출력하도록 하였음
"""
import sys
input = sys.stdin.readline

def pairs(n):
    if n in memo:
        return memo[n]
    left, right = 0, M-1
    while left <= right:
        mid = (left + right)//2
        if B[mid] < n:
            left = mid+1
        else:
            right = mid-1
    return left

ans = []
for _ in range(int(input())):
    memo = {}
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    B.sort()
    cnt = 0
    for a in A:
        cnt += pairs(a)
    ans.append(cnt)
print(*ans, sep='\n')