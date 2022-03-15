'''
입력을 2줄 받아서 첫 입력을 반복해서 돌면서
두번째 입력에 포함되는지 확인
-> 이 과정에서 함정이 있었는데
위 과정 그대로 하면 첫 입력에 a가 3개
두번째 입력에 a가 1개면
aaa가 출력됨
그래서 a-z 딕셔너리 2개를 만들어서 숫자 세고 비교해서 값을 내는 방법으로 해야하는데
이미 작성된 코드를 갈아 엎기 귀찮아서
두번째 입력에서 발견된 캐릭터를 ' '으로 치환하는 것으로 함
지금 보니 위의 방법보다 나아 보이기도 하고?

포함되면 dict에 추가하고
마지막에 dict를 튜플을 항으로 가진 list로 변환하여 정렬하고
그걸 튜플의 각 항끼리 곱해서(문자열 * 정수 꼴) list로 만들고
이걸 join함수로 문자열로 만들어 출력함
'''
while True:
    try:  # 문제가 이상한 문제
        # 입력 값을 받아옴
        a = input()
        # if not a: # 입출력에 문자열 길이 0이 있어서 요렇게 풀면 안됨
        #     break
        b = input()
        _dict = {}

        # a의 캐릭터가 b에 존재하는지 확인하여 _dict에 넣고 카운트 함
        for char in a:
            if char == ' ':
                continue
            if char in b:
                b = list(b)
                b[b.index(char)] = ' ' # 기존의 코드를 안 날리고 그대로 쓰느라 이렇게 더러워짐ㅋㅋ
                _dict.setdefault(char, 0)
                _dict[char] += 1

        # _dict를 list로 변환하여 알파벳 순으로 정렬함
        ans_list = sorted(list(_dict.items()), key = lambda tuple: tuple[0])

        # 정렬된 튜플을 맵 함수로 값을 뽑아서 곱하고(알파벳 개수만큼 연속된 스크링이 됨)
        # 다시 리스트로 만들어 join함수로 공백없이 붙여서 출력함
        print(''.join(list(map(lambda dict: dict[0]*dict[1], ans_list))))
    except EOFError:
        break