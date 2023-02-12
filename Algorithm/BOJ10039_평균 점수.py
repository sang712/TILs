"""
입력을 받고 합계를 낼 때 해당 점수가 40점 이하인 경우 40을 더하는 방식으로 합계를 내고
평균을 내서 출력하였음
"""
total = 0
for _ in range(5):
    score = int(input())
    total += score if score > 40 else 40
print(total//5)