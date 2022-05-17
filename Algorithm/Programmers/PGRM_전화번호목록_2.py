# 출처: 프로그래머스 - 다른 사람의 풀이

def solution(phone_book):
    # answer = True

    # 전화번호 딕셔너리로 저장
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1

    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            # 이 부분에서 in으로 체크할 때 해시를 사용하는 dictionary가 더 빠름
            if temp in hash_map and temp != phone_number:
                # answer = False # 여기서 return을 해주지 않으면 모든 전화번호를 돌기때문에 프루닝
                return False
    # return answer