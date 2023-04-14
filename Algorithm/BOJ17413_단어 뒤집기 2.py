"""
인풋이 크면 시간 초과가 날 수도 있는 문제
태그가 사용 되었으면 태그가 끝날 때까지 그냥 list에 집어넣고
태그가 사용되지 않았으면 누적해서 저장하다가
공백이 나타나거나 태그가 시작되면 뒤집에서 리스트에 넣는 방식으로 구현하였음
뒤집는 연산을 사용하지 안았다면 더 빠른 결과가 나오지 않았을까 생각이 듦
"""
S = input()

output_S = []
is_tag = False
word = ''
for char in S:
    
    if char == '<':
        is_tag = True
        output_S.extend(list(word)[::-1])
        word = ''
    
    if is_tag:
        output_S.append(char)
        if char == '>':
            is_tag = False
    else:
        if char == ' ':
            output_S.append(word[::-1] + ' ')
            word = ''
            continue
        word += char
            
if word:
    output_S.extend(list(word)[::-1])

print(''.join(output_S))