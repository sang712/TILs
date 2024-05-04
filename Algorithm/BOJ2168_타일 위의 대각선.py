"""
gcd를 구해서 계산하기 전에 나눠주고 계산 끝나고 다시 곱해주면 되겠다고 생각해서
우선 gcd를 구했고
대각선을 그릴 때 큰 수에서 작은 수로 나눠서 올림하면
작은 수를 기준으로 하는 축이 1이 증가할 때마다 지나는 칸의 개수를 구할 수 있어서
이 수에 작은 수를 곱하고 여기에 다시 gcd를 곱해 답을 출력했는데 틀렸다고 했음

근데 잘 보니까 규칙이 보여서 해당 방법으로 수정하였음
지나쳐야하는 칸은 가로 칸을 모두 지나야 하므로 가로 칸 수에
세로 칸도 모두 지나야 하므로 세로 칸 수를 더한 뒤에 1을 빼 주는 방식임
1을 빼는 이유는 가로 1줄 짜리로 생각해보면 이미 가로 칸을 세는데에 세로 칸 1줄이 포함되기 때문
"""
x, y = map(int, input().split())

def gcd(a, b):
    if a % b == 0: return b
    return gcd(b, a % b)

_gcd = gcd(x, y)
x //= _gcd
y //= _gcd

print((x+y-1) * _gcd)
# _gcd = gcd(x, y)
# small = min(x, y) // _gcd
# big = max(x, y) // _gcd

# print(small * (big//small + int(big%small>0)) * _gcd)