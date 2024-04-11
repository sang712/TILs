"""
각 행과 열을 각각 확인하면서 #을 기준으로 문자열을 나누고
해당 문자열들을 다시 확인하면서 길이가 2 이상이면 단어로 판단해 따로 저장하였음
그 후에 저장한 문자들을 정렬하여 가장 순서가 앞서는 단어를 출력하였음
"""
R, C = map(int, input().split())
crossword = [input() for _ in range(R)]

words = []
for row in crossword:
    r_words = row.split('#')
    for word in r_words:
        if len(word) > 1:
            words.append(word)
    
for col in zip(*crossword):
    c_words = ''.join(col).split('#')
    for word in c_words:
        if len(word) > 1:
            words.append(word)  
words.sort()
print(words[0])