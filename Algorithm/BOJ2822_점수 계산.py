"""
점수와 입력 순서를 튜플 쌍으로 하여 리스트에 저장하고 정렬한 뒤
가장 높은 점수 5개를 사용하여 합과 문제 번호를 출력하였음
"""
quiz_score = []

for i in range(1, 9):
    quiz_score.append((i, int(input())))
    
quiz_score.sort(key=lambda x: -x[1])
quiz_num, score = zip(*quiz_score[:5])
print(sum(score))
print(*sorted(quiz_num))