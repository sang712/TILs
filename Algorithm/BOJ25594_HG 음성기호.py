"""
index를 따라가며 첫 알파벳으로 시작하는 글자가 HG 음성기호와 알맞으면 해당 길이만큼
건너뛰어 다시 확인하는 과정을 반복하여 변환을 하고 변환된 글자를 모아 출력하였음

712ms가 나와서 replace 함수를 이용해 시간 단축을 꾀하여 보았으나
yahoosolvedac과 같은 예시에서는 os를 먼저 찾아버리는 문제가 발생하였음

이 글을 작성하면서 보니 문제가 될만한 부분은 os 부분밖에 없어서 
역순으로 탐색하였더니 통과하였음
그 중 가능성이 컸던 iu의 경우는 i로 끝나는 음성기호가 없어서 무시할 수 있었음
"""
hg = {'a': 'aespa', 'b': 'baekjoon', 'c': 'cau', 'd': 'debug', 'e': 'edge', 
'f': 'firefox', 'g': 'golang', 'h': 'haegang', 'i': 'iu', 'j': 'java', 
'k': 'kotlin', 'l': 'lol', 'm': 'mips', 'n': 'null', 'o': 'os', 
'p': 'python', 'q': 'query', 'r': 'roka', 's': 'solvedac', 't': 'tod', 
'u': 'unix', 'v': 'virus', 'w': 'whale', 'x': 'xcode', 'y': 'yahoo', 
'z': 'zebra'}

S = input()
for key in list(hg.keys())[::-1]:
    S = S.replace(hg[key], f' {key.upper()} ')
ans = S.split()

for a in ans:
    if len(a) > 1 or a.islower():
        print('ERROR!')
        break
else:
    print("It's HG!")
    print(''.join(ans).lower())
# hg = {'a': 'aespa', 'b': 'baekjoon', 'c': 'cau', 'd': 'debug', 'e': 'edge', 
# 'f': 'firefox', 'g': 'golang', 'h': 'haegang', 'i': 'iu', 'j': 'java', 
# 'k': 'kotlin', 'l': 'lol', 'm': 'mips', 'n': 'null', 'o': 'os', 
# 'p': 'python', 'q': 'query', 'r': 'roka', 's': 'solvedac', 't': 'tod', 
# 'u': 'unix', 'v': 'virus', 'w': 'whale', 'x': 'xcode', 'y': 'yahoo', 
# 'z': 'zebra'}

# S = input()
# ans = []
# i = 0
# while i < len(S):
#     s = S[i]
#     code = hg[s]
#     leng = len(code)
#     if S[i:i+leng] == code:
#         ans.append(s)
#         i += leng
#     else:
#         print('ERROR!')
#         break
# else:
#     print("It's HG!")
#     print(''.join(ans))
