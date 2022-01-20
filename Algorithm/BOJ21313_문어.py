# 사전상에서 가장 우선이려면 1 2의 반복으로 이루어져야함
# 따라서 짝수면 1 2의 반복 홀수이면 1 2로 반복하다 3으로 끝나도록
N = int(input())

ans = ''
for i in range(1, N+1):
    if i == 1:
        ans += str(i) + ' '
    else:
        if i % 2:
            if i == N:
                ans += '3 '
            else:
                ans += '1 '
        else:
            ans += '2 '

print(ans.strip())