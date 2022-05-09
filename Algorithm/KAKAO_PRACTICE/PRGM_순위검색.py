from itertools import combinations as combi
from bisect import bisect_left

def solution(info, query):
    answer = []
    # ['조건', [점수들]] 형태로 주어진 정보 정리, 조건에 '-'를 추가해서 작성
    combi_dict = {}
    for idx, value in enumerate(info):
        information = list(value.split())
        condition = information[:-1]
        score = int(information[-1])
        for i in range(5):
            combinations = list(combi([0,1,2,3], i))
            for comb in combinations:
                temp = condition.copy()
                for idx in comb:
                    temp[idx] = '-'
                key = ''.join(temp)
                combi_dict.setdefault(key, [])
                combi_dict[key].append(score)
    
    # 주어진 정보의 점수를 정렬
    for value in combi_dict.values():
        value.sort()
    
    # 찾는 쿼리를 이용해서 정보에서 찾음, 이분탐색을 이용
    for idx, value in enumerate(query):
        
        temp = list(value.replace('and', '').split())

        condition = ''.join(temp[:-1])
        score = int(temp[-1])
    
        count = 0
        if condition in combi_dict:
            incondition = combi_dict[condition]
            idx = bisect_left(incondition, score)
            count = len(incondition) - idx
        answer.append(count)

    return answer