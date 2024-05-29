"""
최댓값을 제외한 전체 합이 최댓값보다 작으면 최댓값이 정답이고
그렇지 않으면 전체 값을 2로 나눈 값이 정답인데
이 때 최댓값을 제외한 나머지의 합을 최댓값과 함께 지울 수 있기 때문에
이 값을 지우고 났을 때 남는 값이 짝수인지 홀수인지를 판별해 답에 더해줌
"""
N = int(input())
houses = list(map(int, input().split()))
houses.sort(reverse=True)

max_snow = houses[0]
sum_snow = sum(houses)
ans = 0
if sum_snow - max_snow <= max_snow:
    ans = max_snow
else:
    ans = sum_snow // 2 + (sum_snow - 2 * max_snow) % 2
print(-1 if ans > 1440 else ans)