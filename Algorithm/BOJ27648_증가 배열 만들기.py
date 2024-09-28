"""
1부터 M까지 되는 1차원 배열을
모든 원소의 값을 1부터 N씩을 더하면서 2차원 배열을 만들었음
처음에는 반복문으로 처음부터 만들면서 바로바로 출력해서 332ms
그 다음에는 모두 만들어서 한번에 출력해서 196ms
그 후에는 1차원 배열을 처음부터 만드는 것이 아니라 맨 앞 pop 맨 뒤 append 해서 구해서 76ms
"""
N, M, K = map(int, input().split())
if N + M - 1 <= K:
    print('YES')
    ans = []
    temp = list(map(str, range(1, 1+M)))
    for i in range(1, N+1):
        ans.append(' '.join(temp))
        temp.pop(0)
        temp.append(str(i+M))
    print(*ans, sep='\n')
else:
    print('NO')
