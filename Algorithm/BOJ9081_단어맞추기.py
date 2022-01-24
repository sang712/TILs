# list 형태를 스트링으로 풀어서 넣으려면 ''.join() 함수를 이용하기
# 스트링 사이에 구분자가 필요하면 '구분자'.join()과 같이 사용하기
"""
이 문제는 next_permutation 함수의 로직을 따라 만든 것임
끝에서부터 앞으로 오면서 바로 뒤의 것보다 작은 것을 i로 두고
다시 끝에서부터 앞으로 오면서 i의 값보다 큰 값을 j로 두고
i와 j의 값을 서로 맞 바꾼다
그리고 원래 i의 위치 이후의 값을 정렬하면 된다.
"""

T = int(input())

for _ in range(T):
    word = input()
    length = len(word)
    former = length
    latter = -1
    for i in range(length-1, -1, -1):
        if i == length-1:
            continue
        else:
            if ord(word[i]) < ord(word[i+1]):
                former = i
                break
    for j in range(length-1, former, -1):
        if ord(word[former]) < ord(word[j]):
            latter = j
            break
    next_word = list(word)
    if former < 0 or latter < 0:
        print(word)
        continue
    next_word[former], next_word[latter] = next_word[latter], next_word[former]
    next_word = next_word[:former+1] + sorted(next_word[former+1:])

    print(f'{"".join(next_word)}')