"""
6개의 단어 중 3개를 줄지어 나열하는 순열을 구한 뒤
zip 함수로 가로 세로를 뒤집고 단어로 변환한 뒤에
처음 선택한 세 단어와 만들어진 세 단어를 더해 정렬하여 총 6개의 단어 무리와 같을 때
답으로 출력하였음
"""
words = [input() for _ in range(6)]
words.sort()
ans = []
have = [0]*6
def choose(rows, n):
    if n < 3:
        for i in range(6):
            if not have[i]:
                rows.append(words[i])
                have[i] = 1
                choose(rows, n+1)
                rows.pop()
                have[i] = 0
    else:
        new_words = sorted(list(map(''.join, zip(*rows))) + rows)
        if new_words == words:
            ans.append('\n'.join(rows))
choose([], 0)

if ans:
    print(ans[0])
else:
    print(0)