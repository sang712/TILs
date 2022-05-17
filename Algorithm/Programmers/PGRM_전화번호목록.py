def solution(phone_book):
    answer = True
    
    # 소트 하면 짧은 문자열이 우선이 되는 점을 이용하여 판단
    phone_book.sort()
    for i in range(1, len(phone_book)):
        if phone_book[i].startswith(phone_book[i-1]):
            answer = False
            break
        else:
            continue

    return answer