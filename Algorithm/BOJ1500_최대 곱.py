"""
S를 K로 나눈 숫자를 이용해 곱하면 최대 곱이 나온다는 것을 이해했지만
곱한 수의 개수가 1이상의 K개의 수여야 한다는 것을 간과하여
틀린 답을 만들었음
수정한 답은 다음과 같이 풀이하였음
S // K 값을 먼저 구하고
여기에 S가 아직 남아 있다면 1씩 더해준 뒤에 누적해서 곱하는 방식으로 풀이를 수정하였음
"""
S, K = map(int, input().split())

div = S // K
S -= div * K

ans = 1
for _ in range(K):
    if S:
        ans *= (div + 1)
        S -= 1
    else:
        ans *= div

print(ans)