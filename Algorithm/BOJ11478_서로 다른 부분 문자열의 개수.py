"""
반복문으로 슬라이싱 해서 셋에 넣고 셋의 길이를 출력하였음
"""
S = input()
sub = set()
for i in range(len(S)):
    for j in range(i+1, len(S)+1):
        sub.add(S[i:j])
print(len(sub))