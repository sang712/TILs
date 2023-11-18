"""
답을 담고 있는 리스트를 정해두고 답을 찾을 때마다 넣는 방식으로 초기화 함
답을 찾은 상태면 바로 반복문을 중단하도록 했고 그것이 아니라면 계속 찾도록 함
"""
N, H, W = map(int, input().split())

ans = ['?'] * N
for h in range(H):
    damaged_string = input()
    for n in range(N):
        for w in range(W):
            if ans[n] != '?':
                break
            if damaged_string[n * W + w] != '?':
                ans[n] = damaged_string[n * W + w]
print(*ans, sep='')