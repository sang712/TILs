# 출처: 프로그래머스 - 다른 사람의 풀이

# Counter 클래스를 사용한 풀이
# Counter는 객체를 자동으로 분해하여 딕셔너리 형태로 카운트 함
# ex) 문자열 -> 문자, 리스트 -> 리스트 인자
import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]