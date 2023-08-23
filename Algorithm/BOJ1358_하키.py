"""
경기장의 사각형 안에 들어오는지 판단하고
그렇지 않다면 경기장의 반원의 중점에서 거리가 얼마가 되는지 확인하여 카운트 하였음
"""
W, H, X, Y, P = map(int, input().split())
left = (X, Y + H // 2)
right = (X + W, Y + H // 2)
ans = 0
def dist(x1, y1, x2, y2):
    return abs(x1-x2) ** 2 + abs(y1-y2) ** 2
for _ in range(P):
    p_x, p_y = map(int, input().split())
    if Y <= p_y <= Y + H:
        if X <= p_x <= X + W:
            ans += 1
        elif dist(*left, p_x, p_y) <= (H // 2) ** 2 or dist(*right, p_x, p_y) <= (H // 2) ** 2:
            ans += 1
print(ans)
	