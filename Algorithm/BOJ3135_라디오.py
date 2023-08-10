"""
저장된 채널로 이동할 때는 총 버튼 횟수에 1을 더했고
위아래로만 이동한 경우에는 그냥 횟수를 세어 비교한 뒤 출력하였음
"""
A, B = map(int, input().split())
N = int(input())
channels = [int(input()) for _ in range(N)]

ans = []
ans.append(abs(A - B))
for channel in channels:
    ans.append(abs(B - channel) + 1)

print(min(ans))