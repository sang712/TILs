"""
입찰가를 동시에 똑같이 올리므로 각각의 정보는 필요없고
a와 b의 차이만을 얻어서 정렬한 뒤에
K번째의 입찰가의 차이만큼 올리면 최소 K개만큼 낙찰을 받을 수 있음
여기에 차이가 음수일 경우 0으로 만들도록 max함수를 사용함
"""
N, K = map(int, input().split())
bids = []
for _ in range(N):
    a, b = map(int, input().split())
    bids.append(b-a)
bids.sort()
print(max(0, bids[K-1]))
