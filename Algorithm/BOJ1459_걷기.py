"""
예제에 2 0 12 10 이 없었다면 틀렸을 문제
대각선으로만 움직여서 2칸씩 갈 수 있다는 것을 간과한다면 틀리는 문제
한줄 식으로 표현하여 풀었음
"""
X, Y, W, S = map(int, input().split())
ans = min(X, Y) * min(2 * W, S) + (abs(X - Y)//2) * 2 * min(W, S) + (abs(X - Y) % 2) * W
print(ans)