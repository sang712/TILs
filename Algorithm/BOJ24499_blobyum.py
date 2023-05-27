"""
처음 파이를 받아서 저장하고
먹을 파이의 개수만큼 합계를 낸 뒤에 
반복문을 돌면서 가장 앞의 파이를 빼고 맨뒤에 파이를 더하는 방식으로(슬라이딩 윈도우) 풀이하였음
"""
N, K = map(int, input().split())
pies = list(map(int, input().split()))

maximum_pies = serial_pies = sum(pies[:K])
for i in range(N):
    serial_pies -= pies[i]
    serial_pies += pies[(K + i) % N]
    if serial_pies > maximum_pies:
        maximum_pies = serial_pies
        
print(maximum_pies)
