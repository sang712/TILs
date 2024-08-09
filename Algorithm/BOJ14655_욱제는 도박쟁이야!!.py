"""
연속해서 3개씩을 뒤집는다고는 했지만
횟수 제한이 없고 좌우 끝에서도 자유롭게 뒤집을 수 있어서
결과적으로는 그냥 원하는 동전만 뒤집을 수 있음
그래서 모든 수의 절댓값을 구했음
"""
N = int(input())
first_round = map(int, input().split())
second_round = map(int, input().split())
ans = 0
for coin in first_round:
    if coin >= 0:
        ans += coin
    else:
        ans -= coin
for coin in second_round:
    if coin >= 0:
        ans += coin
    else:
        ans -= coin
print(ans)