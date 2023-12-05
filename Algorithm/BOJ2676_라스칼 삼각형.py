"""
라스칼 삼각형을 그려보면 규칙성을 찾아볼 수 있음
그 규칙을 수식화 해서 풀이하였음
"""
ans = []

for t in range(int(input())):
    n, m = map(int, input().split())
    ans.append(1 + m * (n - m))
    
print(*ans, sep='\n')