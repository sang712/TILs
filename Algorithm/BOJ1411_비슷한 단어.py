"""
각 문자를 이중 for문으로 돌면서 겹치지 않는 쌍으로 확인하고
이 때 각 문자열의 문자를 쌍과 어느 것으로 변하는지를 각각 저장한 뒤에
문자열의 문자를 또 for문으로 돌면서
문자의 쌍이 없고 그 문자로 변하지도 않았으면 저장하고 넘어가고
문자의 쌍이 없고 그 문자로 변한 적이 있으면 해당 쌍 포기
문자의 쌍이 있는데 변한 과정이 다르면 해당 쌍 포기
모든 문자가 그 외의 경우를 만족하면 문제에서 제시한 비슷한 문자열 쌍이 맞으므로 1카운팅 하는 방식으로 풀이하였음
"""
import sys
input = sys.stdin.readline

N = int(input())

words = [input() for _ in range(N)]
length = len(words[0]) - 1

ans = 0
for i in range(N):
    for j in range(i+1, N):
        check_table = {}
        change_to = set()
        for k in range(length):
            s1 = words[i][k]
            s2 = words[j][k]
            if not s1 in check_table:
                if not s2 in change_to:
                    check_table[s1] = s2
                    change_to.add(s2)
                    continue
                else:
                    break
            if not check_table[s1] == s2:
                break
        else:
            ans += 1
print(ans)
            
        