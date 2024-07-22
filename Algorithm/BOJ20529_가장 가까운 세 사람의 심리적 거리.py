"""
같은 특성의 사람이 3명이 되면 무조건 0이 나오니까
같은 특성이 3명인 특성이 1이상 존재할 수 있는 33명 부터는 0을 바로 출력하도록 하였고
그 이외의 경우에는 3중 for문을 이용해 비교 판단 하여 출력하였음

580ms 나오는 내 답과는 달리 92ms 나오는 답을 확인했더니 
mbti를 비트로 바꾸고 각 3개의 쌍의 점수를 구해 놓은 뒤에 그 점수를 참고하는 방식으로 했음
비트 연산은 좀 더 이해가 필요한 것 같아서 내가 할 수 있는 방식으로 비슷하게 만들었더니 
180ms로 시간 단축을 할 수 있었음
"""
import sys
input = sys.stdin.readline

mbti = ['ISTJ', 'ISFJ', 'INFJ', 'INTJ', 'ISTP', 'ISFP', 'INFP', 'INTP', 
        'ESTP', 'ESFP', 'ENFP', 'ENTP', 'ESTJ', 'ESFJ', 'ENFJ', 'ENTJ']
dist_table = {(a, b, c): 12-sum([int(a[i] == b[i]) + int(b[i] == c[i]) + int(c[i] == a[i]) for i in range(4)]) for a in mbti for b in mbti for c in mbti}
ans = []
T = int(input())
for t in range(T):
    N = int(input())
    people = input().split()
    if N > 32:
        ans.append(0)
        continue
    min_dist = 12
    for i in range(N-2):
        for j in range(i+1, N-1):
            for k in range(j+1, N):
                dist = dist_table[(people[i], people[j], people[k])]
                min_dist = min(min_dist, dist)
    ans.append(min_dist)
print(*ans, sep='\n')