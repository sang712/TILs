'''
입찰가를 키값으로 하고 
입찰자와 입찰 순서를 담은 튜플을 담은 리스트를 값으로 갖는 딕셔너리 구조를 사용하였음
{'입찰가': [(입찰자, 입찰 순서), (입찰자, 입찰 순서)], '입찰가': [(입찰자, 입찰 순서)]}
'''
import sys
input = sys.stdin.readline

U, N = map(int, input().split())
bids = {}
for i in range(N):
    bidder, bid = input().split()
    bids.setdefault(bid, [])
    bids[bid].append((bidder, i))
order = sorted(bids.items(), key=lambda x: (len(x[1]), int(x[0])))
print(sorted(order[0][1], key=lambda x: x[1])[0][0], order[0][0])
    