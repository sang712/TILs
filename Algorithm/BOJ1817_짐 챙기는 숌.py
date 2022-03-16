'''
좌측에서부터 책의 값을 가져와 비교하고
더했을 때 M에서 넘치면
다음에 0에다가 더하는 방식으로 넘김
'''
def solve():
    N, M = map(int, input().split())
    if N == 0:
        print(0)
        return

    cnt = 1
    weight = 0
    books = list(map(int, input().split()))
    for book in books:
        if weight + book <= M:
            weight += book
        else:
            weight = 0 + book
            cnt += 1

    print(cnt)

solve()