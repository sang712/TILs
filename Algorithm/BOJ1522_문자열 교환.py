"""
우선 a의 개수를 세서 a의 개수를 길이로 하는 문자열을 슬라이딩윈도우 방식으로 조사해 
가장 많은 a의 개수를 찾았음
그 뒤에 a의 개수에서 한 슬라이딩 윈도우에 있는 a의 개수를 뺀 뒤에 출력하였음
원형의 문자열이라는 것은 입력받은 문자열을 복사해 이어붙여서 그 뒤까지 다 조사하도록 하여 해결하였음
"""
string = input()
num_a = string.count('a')

string *= 2
max_cnt = cnt = string[:num_a].count('a')
if num_a > 1:
    for i in range(len(string) - num_a):
        if string[i] == 'a':
            cnt -= 1
        if string[i+num_a] == 'a':
            cnt += 1
        if max_cnt < cnt:
            max_cnt = cnt
    print(num_a - max_cnt)
else:
    print(0)