"""
등수보다 적은 수의 금액을 팁으로 주려고 했다면 어차피 0으로 퉁쳐지기 때문에
낮은 금액은 0으로 퉁쳐지게 하고 높은 금액을 주는 사람을 앞에 세우면 됨
따라서 내림차순 정렬을 하고 1원 이상의 금액을 팁으로 주는 사람까지 계산한 뒤에
break를 걸어 나오도록 하였음
자본주의가 낳은 결과물이라고 할 수 있겠음
"""
import sys
input = sys.stdin.readline

N = int(input())
pay_to_gangho = sorted([int(input()) for _ in range(N)], reverse=True)

ans = 0
for i, pay in enumerate(pay_to_gangho):
    if pay > i:
        ans += pay - i
    else:
        break
print(ans)