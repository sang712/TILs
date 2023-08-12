"""
for문으로 반복을 하면서 친구 관계인 사람이 어느 사람인지 저장하고
친구인 사람을 기준으로 그 사람의 친구까지 탐색하는 과정을 통해 답을 구하였음
"""
import sys
input = sys.stdin.readline

N = int(input())
friends = [input().strip() for _ in range(N)]

max_two_friend = 0
for i in range(N):
    two_friends = set()
    for j in range(N):
        friend = friends[i][j]
        if friend == 'Y':
            two_friends.add(j)
            
    for j in two_friends.copy():
        for k in range(N):
            friend = friends[j][k]
            if k != i and friend == 'Y':
                two_friends.add(k)
    max_two_friend = max(max_two_friend, len(two_friends))
print(max_two_friend)
