"""
마지막 풀이 방식처럼 그냥 더하기 빼기만으로 구현하려고 노력해봤는데 잘 되지 않아 그냥 반복문을 이용해 풀이하였음

마지막 풀이는 해당 숫자가 이전까지 등장한 횟수만큼 차감해서 카운팅해서 전체 경우의 수에서 빼는 것인데
숫자가 맞물리는 경우 중복이 되기 때문에 덜 카운트 해주어야 함
이 부분을 계산하기 위해서 어떤 숫자가 같이 등장한 숫자를 따로 저장하고
어느 두 수가 쌍으로 등장했을 때 각각의 숫자와 함께 등장한 숫자가 같은 개수만큼이 여기에 해당함
예를 들어
1 5
1 2
2 3
3 4
4 1
에서 추가로
1 3 이 나온다고 치면
1과 같이 나온 2, 4, 5
3과 같이 나온 2, 4로 2, 4가 동일하게 있기 때문에 2만큼 덜 카운트 해주어야 한다는 뜻

+) 첫 풀이는 2400ms, 두번째 풀이는 540ms 세번째 풀이는 508ms인데
100ms에도 풀어낸 사람이 있어서 궁금함

++) 이것은 입력을 그냥 input으로 받아서 나온 결과고
readline으로 받아온 결과는
1700ms, 244ms, 72ms로 역시 그냥 단순 더하기 빼기가 훨씬 빠른 결과를 얻을 수 있었음
100ms 걸린 사람 때문에 시도해 본 것이었는데 결과적으로 그 사람보다 빠른 결과를 얻어서 뿌듯
"""
N, M = map(int, input().split())

counter = [set() for _ in range(N+1)]
bad_comb = 0
for _ in range(M):
    a, b = map(int, input().split())
    bad_comb += max(N - (2 + len(counter[a]) + len(counter[b]) - len(counter[a].intersection(counter[b]))), 0)
    counter[a].add(b)
    counter[b].add(a)
print(N*(N-1)*(N-2)//6 - bad_comb)


# 첫 풀이
"""
N, M = map(int, input().split())

bad_combs = set()
for _ in range(M):
    a, b = sorted(list(map(int, input().split())))
    for i in range(1, N+1):
        if i == a or i == b:
            continue
        bad_combs.add(tuple(sorted([a, b, i])))
print(N*(N-1)*(N-2)//6 - len(bad_combs))
"""

# 두번째 풀이
"""
N, M = map(int, input().split())

bad_comb = [[0]*(N+1) for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    bad_comb[a][b] = 1
    bad_comb[b][a] = 1

cnt = 0
for i in range(1, N-1):
    for j in range(i+1, N):
        if bad_comb[i][j]: continue
        for k in range(j+1, N+1):
            if bad_comb[i][k] == bad_comb[j][k] == 0:
                cnt += 1
print(cnt)
"""