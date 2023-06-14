yeondu = input()
formula = 'LOVE'

N = int(input())

max_score = 0
team_name = ''
for _ in range(N):
    candidate = input()
    if team_name == '':
        team_name = candidate
        
    num_alphabet = []
    for i in range(4):
        num_alphabet.append(yeondu.count(formula[i]))
    for i in range(4):
        num_alphabet[i] += candidate.count(formula[i])
    
    score = 1
    for i in range(3):
        for j in range(i + 1, 4):
            score *= num_alphabet[i] + num_alphabet[j]
            
    score %= 100
    if score > max_score:
        team_name = candidate
        max_score = score
    elif score == max_score:
        team_name = min(team_name, candidate)
        
print(team_name)