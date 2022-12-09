'''
스킬체크 초보자 2번 문제
파이썬의 스트링 크기 비교를 이용하여 풀었음
스트링 비교까지는 떠올렸는데 다음 방법은 떠올리기 어려웠음
숫자의 크기가 1000까지 이므로 *3해서 반복시켜 숫자가 최소 3자리가 되도록 만들고 정렬하여 join함수로 출력함

데이터가 추가되었는데 '0' '0' 이 들어오면 출력이 '00'이 아닌 '0'이 되어야 해서
해당 부분을 검증하는 부분을 추가하였음
'''
def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key = lambda x: x*3, reverse=True)
    answer = ''.join(numbers)
    while answer.startswith('0') and len(answer) > 1:
        answer = answer[1:]
    return answer