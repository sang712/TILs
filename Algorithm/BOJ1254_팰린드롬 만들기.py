"""
이렇게 쉬운 문제인데 여러번의 시행착오를 겪다니
정신이 빠져있었나봄

우선 뒤에만 문자를 추가할 수 있다는 점을 간과해서 몇 번 틀렸고
그 후에는 연속해야함을 망각하고 endswith가 아닌 in으로 탐색해서 틀렸음
이 경우의 반례가 abcdfefedcb임 bcd가 겹치게 되어 팰린드롬이 있다고 판단하고 18이라는 잘못된 값을 냈음
21이 맞는 출력임
"""
S = input()
length = len(S)

reversed_S = S[::-1]
cnt = 0
for i in range(1, length + 1):
    palindrome = reversed_S[:i]
    if S.endswith(palindrome):
        cnt = i
print(length + length - cnt)