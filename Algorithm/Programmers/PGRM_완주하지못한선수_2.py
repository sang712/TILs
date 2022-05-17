# 출처: 프로그래머스 - 다른 사람의 풀이

# 해시를 사용한 풀이
def solution(participant, completion):
    answer = ''
    temp = 0
    dic = {}
    for part in participant:
        # 해시 값으로 dictionary에 저장
        dic[hash(part)] = part
        # 해시 값들을 모두 더함
        temp += hash(part) # hash는 숫자 값
    for com in completion:
        # 해시 값들을 뺌
        temp -= hash(com)
    # 남은 해시값의 사람을 dictionary에서 뽑아서 출력
    answer = dic[temp]

    return answer