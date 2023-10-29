"""
파일의 길이가 주어져있지 않아서 혹시 몰라 이분탐색을 적용하였음
"""
import sys
input = sys.stdin.readline

N = int(input())
files = [list(map(int, input().split())) for _ in range(N)]

def read_files(k):
    compare_files = set()
    for file in files:
        compare_files.add(tuple(file[:k]))
        
    return len(compare_files) == N

left, right = 1, 2 ** 31
ans = 2 ** 31
while left <= right:
    mid = (left + right) // 2
    if read_files(mid):
        ans = min(ans, mid)
        right = mid - 1
    else:
        left = mid + 1
print(ans)