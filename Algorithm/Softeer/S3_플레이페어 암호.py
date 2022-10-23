'''
문자열을 다루는 구현문제
크게 어렵지는 않았고 문제를 따라가면서 놓친 부분이 없는지 확인하는 것이 핵심
디버깅을 할 때 홀수 번호만 틀려서 이상하게 생각했는데 
마지막이 X하나로 끝날 때를 고려하지 않아서 생긴 문제임을 파악하고 수정해서 제출하여 정답

풀이과정은 딕셔너리에 알파벳을 키값으로 추가된 순서를 값으로 넣었고
해당 값은 암호표의 위치를 계산할 때 사용하였음
좌표상으로 바꾸는 경우가 있어 암호표의 Transpose가 필요하다고 생각했었는데
그럴 필요는 없었음
'''
import sys
message = input()
key = input()

# 암호표 만들기
alphabets = ['A','B','C','D','E','F','G','H','I','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
check = dict()
table = []
cnt = 0
for char in key:
    if not char in check:
        check.setdefault(char, cnt)
        table.append(char)
        cnt += 1
for a in alphabets:
    if not a in check:
        check.setdefault(a, cnt)
        table.append(a)
        cnt += 1
table = [table[:5], table[5:10], table[10:15], table[15:20], table[20:25]]
table_T = list(zip(*table))

# 메시지 나누기
paired = []
i, j = 0, 1
while j<=len(message):
    pair = message[i:j+1]
    if len(pair) == 1:
        if pair == 'X':
            if i == len(message)-1:
                paired.append("XX")
            else:
                paired.append("XQ")
        else:
            paired.append(pair+'X')
        break
        
    if pair[0] == pair[1]:
        if pair == "XX":
            paired.append("XQ")
        else:
            paired.append(pair[0]+"X")
        i += 1
        j += 1
    else:
        paired.append(pair)
        i += 2
        j += 2

# 인코딩하기
def encoding(pair):
    l, r = pair
    li, lj = check[l]//5, check[l]%5
    ri, rj = check[r]//5, check[r]%5
    if li == ri:
        pair = table[li][(lj+1)%5] + table[ri][(rj+1)%5]
    elif lj == rj:
        pair = table[(li+1)%5][lj] + table[(ri+1)%5][rj]
    else:
        pair = table[li][rj] + table[ri][lj]
    return pair

# 결과 출력하기
ans = ""
for pair in paired:
    ans += encoding(pair)
print(ans)