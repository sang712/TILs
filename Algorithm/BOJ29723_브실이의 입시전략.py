"""
입력을 받고
우선 공개된 점수를 모두 더하면서 저장했던 과목에서 제외하고
나머지 점수를 정렬하여 작은 거에서 M-K개, 큰 거에서 M-K개를 각각 더해 답으로 출력하였음
마지막 답을 한 줄로 출력하고 싶었는데
M-K가 0이되는 경우 전체 리스트를 더하게 되어서
해당 부분이 0이 되면 전체 리스트의 길이로 값을 지정하는 코드 한 줄을 추가하였음
"""
import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())

bsil = {}
for _ in range(N):
    subject, score = input().split()
    bsil[subject] = int(score)

ans = 0
for _ in range(K):
    subject = input().strip()
    ans += bsil[subject]
    del bsil[subject]
hidden = sorted(bsil.values())

last_biggest = -(M-K) if M-K else N-M
print(ans + sum(hidden[:M-K]), ans + sum(hidden[last_biggest:]))
