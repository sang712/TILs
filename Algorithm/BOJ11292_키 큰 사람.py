"""
정렬을 하고 가장 큰 사람을 구하는 것 보다 
그냥 완전탐색해서 가장 키가 큰 사람을 찾고 같은 키가 나타나면 거기에 추가하는 방식으로 구현했음
이렇게 풀면 굳이 인덱스 정보 없이도 등장 순서가 지켜지게 됨
"""
import sys
input = sys.stdin.readline

while True:
    N = int(input())
    if N:
        students = [input().split() for _ in range(N)]
    else:
        break
    ans = []
    max_height = 0
    for name, height in students:
        height = float(height)
        if height > max_height:
            max_height = height
            ans = [name]
        elif height == max_height:
            ans.append(name)
    print(*ans)