'''
필요한 금액이 현재 갖고 있는 금액보다 클 때 
그 차액 만큼 출력하도록 하였고
돈이 충분할 경우 0을 출력하였음
'''
K, N, M = map(int, input().split())

price = K * N
print(price - M if price > M else 0)