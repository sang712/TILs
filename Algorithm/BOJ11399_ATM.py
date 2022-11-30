'''
가장 적은 시간이 걸리는 사람을 먼저 두어야 최소로 할 수 있기 때문에
오름차순으로 정렬하였고
먼저온 사람의 시간이 뒷 사람에게 더해지기 때문에
cnt에 앞으로 더해질 회수만큼 곱해서 더해주었음
'''
N = int(input())
P = list(map(int, input().split()))
cnt = 0
P.sort()
for idx, p in enumerate(P):
    cnt += p*(N-idx)
print(cnt)