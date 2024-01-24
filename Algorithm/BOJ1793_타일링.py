"""
점화식을 구한 뒤 dp를 이용해 저장하는 방식으로 풀이하였음
몇 개의 입력이 들어온다는 말이 없었기 때문에 우선 입력부터 다 받도록 하였음
"""
dp = [1, 1]
tc = []
while True:
    try:
       tc.append(int(input())) 
    except:
        break

for i in range(2, max(tc) + 1):
    dp.append(dp[i-1] + dp[i-2] * 2)
for case in tc:
    print(dp[case])