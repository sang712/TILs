"""
T초보다 긴 개미들은 맨 앞과 맨 뒤에 더할 수 있게 하였고
T초안에 움직일 수 있는 개미들은 중간에 번갈아가며 더하여 구현하였음
파이썬의 특성상 인덱스가 음수로 들어가는 경우에 에러가 나는 것이 아니라
다른 답을 출력하기 때문에 틀린답을 내는 원인을 찾기 어려웠는데
범위를 설정하고 나서 문제를 해결할 수 있었음
"""
N1, N2 = map(int, input().split())
group1 = input()[::-1]
group2 = input()
T = int(input())

answer = group1[:N1-T] if N1 > T else ''
for i in range(T):
    if i < len(group2):
        answer += group2[i]
    if 0 <= N1 - T + i < len(group1):
        answer += group1[N1-T+i]
answer += group2[T:]
print(answer)