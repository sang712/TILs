"""
차선이 몇 개로 한정되어있는지 몰라서 그냥 1개일 것이라 가정하고 문제를 풀었음
입력을 받은 뒤에 차의 정보를 dictionary 자료구조로 한 번 더 만들어놓고
나간 차를 확인할 때마다 체크할 수 있도록 하였음
나간 차는 인덱스로 참조하여 
들어간 차를 기준으로 나간 차와 순서대로 비교하여 같으면 다음 들어간 차를 확인하고
같지 않으면 카운팅 하며 계속해서 나간 차를 인덱스를 더해가며 비교하는 방식으로 구현하였음
"""
import sys
input = sys.stdin.readline

N = int(input())
cars_enter = [input().strip() for _ in range(N)]
cars_out = [input().strip() for _ in range(N)]
checked = {car: 0 for car in cars_enter}
ans = 0
idx = 0
for car in cars_enter:
    if checked[car]:
        continue
    while idx < N:
        car_out = cars_out[idx]
        checked[car_out] = 1
        idx += 1
        if car == car_out:
            break
        ans += 1
print(ans)