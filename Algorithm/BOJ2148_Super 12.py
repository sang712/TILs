"""
점수 시스템
라운드 승리시 4점
라운드 무승부시 2점
승패 무관 시도 횟수 4회 이상 1점
패시 득점차 7점 포함 이내이면 1점

등수 시스템
총점 큰 순
라운드 득점 총합 - 피득점 총합 큰 순(abs 아님)
시도 횟수 총합 큰 순
이름 빠른 순

spread는 두 수의 차이를 말하며 왠만하면 양수를 뜻함
"""
teams = {}

while True:
    team = input()
    if team == '#':
        break
    teams[team] = [0, 0, 0, 0, 0]
    
def calculating(info):
    home, away, *numbers = info.split()
    home_score, away_score, home_tries, away_tries = map(int, numbers)
    teams[home] = list(map(sum, zip(teams[home], [0, home_score, away_score, home_tries, away_tries])))
    teams[away] = list(map(sum, zip(teams[away], [0, away_score, home_score, away_tries, home_tries])))
    if home_score > away_score:
        teams[home][0] += 4
        if home_score - away_score < 8:
            teams[away][0] += 1
    elif home_score < away_score:
        teams[away][0] += 4
        if away_score - home_score < 8:
            teams[home][0] += 1
    else:
        teams[home][0] += 2
        teams[away][0] += 2
    if home_tries >= 4:
        teams[home][0] += 1
    if away_tries >= 4:
        teams[away][0] += 1

ans_output = []
round = 1
while True:
    checking_end = input()
    if checking_end == '#':
        break
    calculating(checking_end)
    for _ in range(len(teams) // 2 - 1):
        calculating(input())

    if round > 1:
        ans_output.append('')
    ans_output.append(f'Round {round}')
    
    result = sorted(teams.items(), key=lambda x: (-x[1][0], -x[1][1] - x[1][2], -x[1][3], x[0]))
    for team, numbers in result:
        points, score, score_against, tries, tries_against = map(str, numbers)
        gaps = [' ' * (21 - len(team)), ' ' * (2 - len(points)), ' ' * (4 - len(score)),
                ' ' * (4 - len(score_against)), ' ' * (3 - len(tries)), ' ' * (3 - len(tries_against))]
        ans_output.append(f'{team}{gaps[0]}{gaps[1]}{points}{gaps[2]}{score}{gaps[3]}{score_against}{gaps[4]}{tries}{gaps[5]}{tries_against}')
    
    round += 1
print(*ans_output, sep='\n')