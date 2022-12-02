'''
지표별로 비교하여 선택지에 맞는 결과 값을 더해주는 방식으로 진행했고
어떤 지표가 더 큰 값을 갖고 있는지는 반복되는 부분이라 따로 함수를 만들었음
'''
types = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}

def compare_types(type1, type2):
    if types[type1] > types[type2]:
        return type1
    if types[type1] < types[type2]:
        return type2
    return min(type1, type2)

def solution(survey, choices):
    length = len(survey)
    for i in range(length):
        disagree_type, agree_type = survey[i]
        choice = choices[i]
        if choice < 4:
            types[disagree_type] += 4 - choice
        elif choice > 4:
            types[agree_type] += choice - 4
    answer = ''
    answer += compare_types('R', 'T')
    answer += compare_types('C', 'F')
    answer += compare_types('J', 'M')
    answer += compare_types('A', 'N')
    
    return answer

'''
입출력 예
survey = [["AN", "CF", "MJ", "RT", "NA"], ["TR", "RT", "TR"]]
choices = [[5, 3, 2, 7, 5], [7, 1, 3]]
result = ["TCMA", "RCJA"]
for i in range(2):
    print(f'#{i+1} example')
    print(solution(survey[i], choices[i]))
    print(f'Expected: {result[i]}')
'''