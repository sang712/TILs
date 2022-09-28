'''
재귀를 이용해 조합을 만들어 한 팀에 들어가는 사람들을 골랐고
사람을 다 골랐으면 다른 한 팀에 들어갈 나머지 사람들을 계산해 넣어
시너지 점수를 계산하였음
4588ms 라는 큰 시간이 걸렸음
가장 빠른 사람은 64ms
100ms 대도 많음
'''
N = int(input())
table = [list(map(int, input().split())) for _ in range(N)]

s_players = []
diff = 200
def building(player):
    if len(s_players) >= N//2:
        start = 0
        link = 0
        l_players = [i for i in range(N)]
        for p in s_players:
            l_players.remove(p)
        for p1 in range(N//2):
            for p2 in range(p1, N//2):
                i, j = s_players[p1], s_players[p2]
                start += table[i][j] + table[j][i]
                i, j = l_players[p1], l_players[p2]
                link += table[i][j] + table[j][i]
        global diff
        diff = min(abs(start-link), diff)
        return
    for p in range(player, N):
        s_players.append(p)
        building(p+1)
        s_players.remove(p)
        
building(0)
print(diff)

print(list(zip(table, zip(*table))))
for i, j in zip(table, zip(*table)):
    print(sum(i), sum(j))
print(table[:-1])