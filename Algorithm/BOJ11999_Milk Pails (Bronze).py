"""
dp같은 방식으로 풀이하였음
"""
X, Y, M = map(int, input().split())
m_pail = [0] * (M+1)

m_pail[X] = 1
m_pail[Y] = 1
ans = 0
for i in range(X, M+1):
    if not m_pail[i]:
        continue
    ans = i
    
    if i+X <= M:
        m_pail[i+X] = 1
    if i+Y <= M:
        m_pail[i+Y] = 1
print(ans)
