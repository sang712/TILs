'''
1. 여러개의 구분자로 split 할 경우
-> replace 함수를 이용해 구분자들을 한개의 구분자로 통일
2. startswith 함수
-> startswith 함수는 인자로 str형이나 str로 이루어진 튜플을 받음
따라서 여러개의 조건을 확인하고 싶으면 튜플 형태로 만들어서 인자로 넣으면 됨
대신 리스트를 넣으면 에러가 남
'''
sentence = list(input().replace('-', ' ').split())
abbr = ["c'", "j'", "n'", "m'", "t'", "s'", "l'", "d'", "qu'"]
vowels = ('a', 'e', 'i', 'o', 'u', 'h')

count = 0

for word in sentence:
    count += 1
    for _abbr in abbr:
        # abbr을 튜플로 만들어서 확인해도 되지만
        # abbr 다음에 모음인 것을 확인하기 위해 abbr의 len을 사용하려고
        # 이렇게 코딩을 하였음
        if word.startswith(_abbr) and word[len(_abbr)].startswith(vowels):
            count += 1

print(count)