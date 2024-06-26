"""
개수를 물어보는 문제로
a의 개수는 직전 b의 개수, b의 개수는 직전 a와 b의 각각의 개수의 합이므로
다이다믹 프로그래밍으로 구현하였음
"""
K = int(input())
AB = [(0, 0), (0, 1)]

for _ in range(K):
    a, b = AB[-1]
    AB.append((b, a+b))
    
print(*AB[K])