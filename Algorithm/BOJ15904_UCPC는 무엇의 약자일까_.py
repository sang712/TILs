"""
UCPC 글자를 하나씩 순차적으로 찾으면서
슬라이싱 해서 다음 글자를 찾도록 하였음
"""
def find_UCPC():
    sentence = input()
    is_U = sentence.find('U')
    sentence = sentence[is_U+1:]
    if is_U >= 0:
        is_C = sentence.find('C')
        sentence = sentence[is_C+1:]
        if is_C >= 0:
            is_P = sentence.find('P')
            sentence = sentence[is_P+1:]
            if is_P >= 0:
                is_C = sentence.find('C')
                if is_C >= 0:
                    print('I love UCPC')
                    return True
    print('I hate UCPC')
    return False
find_UCPC()