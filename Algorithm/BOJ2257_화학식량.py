"""
재귀 방식으로 괄호 안에 있는 원자의 개수를 판단하도록 구현하였음
괄호 안의 원자의 개수를 계산한 뒤 괄호를 벗겨낼 때 밖에 숫자가 있으면 같이 곱하도록 하였음
"""
chem_form = input()

def dealing_parenthesis(i):
    elements = {'h': 0, 'c': 0, 'o': 0}
    while i < len(chem_form):
        mark = chem_form[i]
        if mark == '(':
            nh, nc, no, i = dealing_parenthesis(i+1)
            elements['h'] += nh
            elements['c'] += nc
            elements['o'] += no
        elif mark == 'H':
            elements['h'] += 1
        elif mark == 'C':
            elements['c'] += 1
        elif mark == 'O':
            elements['o'] += 1
        elif mark == ')':
            break
        else:
            elements[chem_form[i-1].lower()] += int(mark) - 1
        i += 1
    if i+1 < len(chem_form) and '1' <= chem_form[i+1] <= '9':
        i += 1
        mark = int(chem_form[i])
        elements['h'] *= mark
        elements['c'] *= mark
        elements['o'] *= mark
    return *elements.values(), i

h, c, o, _ = dealing_parenthesis(0)
print(h*1 + c*12 + o*16)