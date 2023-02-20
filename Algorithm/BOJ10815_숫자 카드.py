"""
정렬해서 이분 탐색으로 풀 수도 있었는데 조금더 간편하고 파이썬스러운 방법으로
set 자료구조를 이용하여 풀이하였다.
"""
N = int(input())
cards = set(map(int, input().split()))
M = int(input())
guesses = list(map(int, input().split()))
answer = []
for guess in guesses:
    if guess in cards:
        answer.append(1)
    else:
        answer.append(0)
print(*answer)