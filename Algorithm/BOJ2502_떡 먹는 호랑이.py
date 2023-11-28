"""
우선 첫 날과 둘쨋 날에 준 떡의 개수를 미지수로 잡고
D째 날에 첫 날과 둘쨋 날에 준 떡의 몇 배를 주었는지 계산한 뒤에
브루트 포스 방법으로 a와 b의 값을 추정하였음

브루트 포스 방법으로 하니 시간초과가 나서
a을 구하는 공식을 만들어서 b의 변화에 따른 a값을 계산하고
조건에 맞는지 확인하여 조건에 맞았을 때 루프를 멈추고 출력하도록 하였음
"""
D, K = map(int, input().split())

days = [[1, 0], [0, 1]]
for i in range(2, D):
    days.append(list(map(sum, zip(days[i-1], days[i-2]))))

first, second = days[-1]
for b in range(1, K // second + 1):
    if (K - b*second) % first == 0:
        a = (K - b*second) // first
        if a <= b:
            break
print(a, b, sep='\n')