"""
최근에 풀었던 boj24499번 blobyum 문제와 같이 
처음 m개의 날짜에 해당하는 급여를 모두 더하고 for문으로 반복을 하면서
더한 값에서 가장 첫 값을 빼고 더한 값들의 다음 값을 더하는 방식(슬라이딩 윈도우)으로 풀이하였음
"""
n, m = map(int, input().split())
Ts = list(map(int, input().split()))

max_income = income = sum(Ts[:m])
for i in range(n-m):
	income -= Ts[i]
	income += Ts[i + m]
	if income > max_income:
		max_income = income
print(max_income)