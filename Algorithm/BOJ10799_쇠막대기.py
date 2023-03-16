"""
스택 문제이지만 입력에서 예외 경우없이 입력된다고 정의 해주었으므로 스택은 사용하지 않았음
겹친 쇠막대의 수와 조각들의 수를 각각 카운트하여 출력하도록 하였음
"""
rod_n_laser = input().replace('()', 'l')

layer = 0
pieces = 0
for s in rod_n_laser:
    if s == '(':
        pieces += 1
        layer += 1
    elif s == 'l':
        pieces += layer
    elif s == ')':
        layer -= 1
print(pieces)
    