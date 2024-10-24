"""
정렬하여 양 끝 값을 더하면서 X값보다 작으면 X값으로 갱신하는 방법으로 풀이하였음
"""
import sys
input = sys.stdin.readline

N = int(input())
students = sorted([int(input()) for _ in range(N)])
X = 2_000_000
for i in range(N//2):
    X = min(X, students[i]+students[-(i+1)])
print(X)
