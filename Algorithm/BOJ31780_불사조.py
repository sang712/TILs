"""
문제에서 요구한대로 구현해 봤는데
더 빠른 속도로 푼 사람이 있어서 고민한 결과
x * (m+1)이 답이라는 것을 알 수 있었음
"""
X, M = map(int, input().split())

print(X*(M+1))
# X, M = map(int, input().split())

# fonixes = [X]
# ans = X
# for _ in range(M):
#     temp = []
#     for x in fonixes:
#         a = x // 2
#         b = x-a
#         temp.extend([a, b])
#     fonixes = temp
#     ans += sum(fonixes)
# print(ans)