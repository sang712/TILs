"""
입력 범위가 30000까지라 브루트포스로 풀이가 가능하다고 생각했고
두번째 숫자가 첫번째 수의 절반보다는 커야 한다고 결론지어서 다음과 같이 풀이하였음
단 추가로 1일 경우를 고려하기 위해 탐색 범위를 N+1까지 해주었음
"""
N = int(input())
max_length = 2
ans = None
for i in range(N//2+1, N+1):
    sequence = [N, i]
    while sequence[-2] - sequence[-1] >= 0:
        sequence.append(sequence[-2] - sequence[-1])
    if len(sequence) > max_length:
        max_length = len(sequence)
        ans = sequence
    elif len(sequence) < max_length:
        break
print(len(ans))
print(*ans)