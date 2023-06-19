'''
제한 조건에 따라 S에는 n보다 큰 수는 무조건 있지만 n보다 앞서는 수가 없을 수 있으므로
해당 부분을 다음과 같이 예외 처리 하였음

S에 속한 수가 1개 인 경우 
일단 n보다 큰 수는 무조건 존재하므로 이 수를 찾는 것으로하고
그 다음에 이 수보다 작은 수가 있는지 없는지를 Error 체킹으로 걸르면서 확인하고
그러고 n이 범위의 오른쪽 끝, 왼쪽 끝일경우, 포함되는 경우 이 세가지 경우를 더하기
'''
L = int(input())
S = list(map(int, input().split()))
n = int(input())

if n in set(S):
    print(0)
else:
    S.sort()
    the_number = idx = ans = 0
    for i, s in enumerate(S):
        if s > n:
            the_number = s
            idx = i
            break
    if idx:
        prev_number = S[idx - 1]
    else:
        prev_number = 0
    left_gap = n - prev_number - 1
    right_gap = the_number - n - 1
    ans = left_gap + right_gap + left_gap * right_gap
    print(ans)