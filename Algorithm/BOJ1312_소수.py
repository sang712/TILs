"""
float은 유효숫자 16개까지만 보여주기 때문에 그냥 나눠버리면 안 되고
초등학교 수업시간에 배운 방식인 원시적인 방식으로 해야함
왜 이런 방법으로 풀 생각을 못 했는지 모르겠음
"""
A, B, N = map(int, input().split())

rest = A % B
decimal_digits = []
while len(decimal_digits) <= N:
    if rest >= B:
        digit, rest = divmod(rest, B)
        decimal_digits.append(digit)
    else:
        decimal_digits.append(0)
    rest *= 10

print(decimal_digits[-1])