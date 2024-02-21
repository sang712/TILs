"""
N의 범위가 주어지지 않아서 이렇게 오래 걸릴 줄 몰랐는데 5000ms가 걸렸음
슬라이딩 윈도우 방식을 사용했고
1부터 N까지 돌도록 했고
시간을 절약하기 위해 숫자 본인을 미리 카운팅하고 
N/2까지 확인하도록 수정해서 3400ms로 줄일 수 있었음
"""
N = int(input())
half_N = N // 2
start, end = 1, 2
ans = 1
sumation = 3
while start <= end < N:
    if sumation < N:
        end += 1
        sumation += end
    elif sumation > N:
        sumation -= start
        start += 1
    else:
        ans += 1
        end += 1
        sumation += end
    if start > half_N + 1:
        break
print(ans)