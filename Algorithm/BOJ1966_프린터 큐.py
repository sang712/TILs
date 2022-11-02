import sys
input = sys.stdin.readline

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    documents = list(map(int, input().split()))
    orders = [i for i in range(N)]
    cnt = 0
    while documents:
        priority = documents[0]
        for i in range(1, len(documents)):
            if documents[i] > priority:
                documents.append(documents.pop(0))
                orders.append(orders.pop(0))
                break
        else:
            documents.pop(0)
            order = orders.pop(0)
            cnt += 1
            if order == M:
                break
    print(cnt)