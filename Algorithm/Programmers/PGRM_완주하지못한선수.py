def solution(participant, completion):
    answer = ''
    
    finisher = dict()
    # 완주한 선수 dictionary에 카운트
    for person in completion:
        finisher.setdefault(person, 0)
        finisher[person] += 1
    
    # 완주자 dictionary에서 참가자와 비교하여 카운트 뺄셈
    for person in participant:
        if person in finisher and finisher[person] > 0:
            finisher[person] -= 1
        else:
            answer = person
            break
            
    return answer