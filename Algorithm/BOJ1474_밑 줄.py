"""
정렬이 필요한 문제인 줄 알았는데 정렬은 필요 없었고
'_'가 추가적으로 필요한 개수를 센 다음 순차로 돌면서 소문자로 시작하면 하나씩 추가하고
만약 소문자 앞에 추가하고도 남는다면 뒤에서부터 순차로 돌면서 대문자로 시작하면 하나씩 추가하는 방식으로 풀이하였음
"""
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

words = []
for _ in range(N):
    word = input().strip()
    M -= len(word)
    words.append(word)

ans = []
div, mod = divmod(M, N-1)
for i in range(N):
    word = words[i]
    if i > 0:
        num_dash = div
        if word[0].islower() and mod > 0:
            num_dash += 1
            mod -= 1
        word = '_' * (num_dash) + word
    ans.append(word)

if mod > 0:
    for i in range(N-1, 0, -1):
        word = words[i]
        if word[0].isupper():
            if mod > 0:
                ans[i] = '_' + ans[i]
                mod -= 1
            else:
                break

print(*ans, sep='')