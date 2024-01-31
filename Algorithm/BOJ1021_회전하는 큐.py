"""
입력의 크기가 50을 넘지 않아서 그냥 pop을 사용하지 않고 리스트를 그대로 사용하였음
값이 빠져나간 부분에는 나올 수 없는 값인 0을 넣어놓고
탐색을 할 때 0을 만나면 카운팅을 하지 않는 방식으로 구현하였음
"""
N, M = map(int, input().split())
nums = list(map(int, input().split()))

q = list(range(1, N + 1))
cur_length = N
cur_location = 0
ans = 0
for num in nums:
    cnt = 0
    while q[cur_location] != num:
        if q[cur_location]:
            cnt += 1
        cur_location = (cur_location + 1) % N
    q[cur_location] = 0
    cur_location = (cur_location + 1) % N
    ans += min(cur_length - cnt, cnt)
    cur_length -= 1
print(ans)