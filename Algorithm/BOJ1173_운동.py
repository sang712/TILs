"""
운동을 하지 못 하는 경우는
최소와 최대 심박수의 차이가 운동을 1분 했을 때의 증가량 보다 작은 경우이므로
해당 경우를 제외하고 계속 while문을 돌면서 운동과 휴식을 반복하도록 하였음
"""
N, m, M, T, R = map(int, input().split())

time_for_excercise = 0
ans = 0
X = m
while m + T <= M:
    if X + T <= M:
        X += T
        ans += 1
        time_for_excercise += 1
    else:
        X -= R
        ans += 1
        if X < m:
            X = m
    if time_for_excercise == N:
        break
else:
    ans = -1
print(ans)